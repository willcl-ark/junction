import json
import os
import os.path
from collections import OrderedDict
from decimal import Decimal
from os import listdir
from pathlib import Path
from shutil import copyfile

from bitcoinrpc.authproxy import AuthServiceProxy
from flask import flash
from hwilib import commands
from hwilib.devices import coldcard, ledger, trezor

home = os.path.expanduser("~")
junction_path = home + "/.junction/"

here = Path(__file__).parent
python_src_dir = Path(here).parent


class JunctionError(Exception):
    pass


### io


def write_json_file(data, filename):
    with open(filename, "w") as f:
        return json.dump(data, f, indent=4)


def read_json_file(filename):
    with open(filename, "r") as f:
        return json.load(f, object_pairs_hook=OrderedDict)


### HWI


def get_client_and_device(fingerprint):
    # get device
    devices = commands.enumerate()
    device = None
    for d in devices:
        if d.get("fingerprint") == fingerprint:
            device = d
    assert device is not None

    # get client
    if device["type"] == "ledger":
        client = ledger.LedgerClient(device["path"])
    elif device["type"] == "coldcard":
        client = coldcard.ColdcardClient(device["path"])
    elif device["type"] == "trezor":
        client = trezor.TrezorClient(device["path"])
    else:
        raise JunctionError(f'Devices of type "{device["type"]}" not yet supported')
    client.is_testnet = True

    return client, device


### wallets


def get_first_wallet_name():
    if not os.path.exists(junction_path + "wallets"):
        os.makedirs(junction_path + "wallets")
    file_names = listdir(junction_path + "wallets")
    if not file_names:
        return None
    file_name = file_names[0]
    return file_name.split(".")[0]


### settings


def make_junction_dir():
    if not os.path.exists(junction_path):
        os.makedirs(junction_path)


def get_settings():
    if not os.path.isfile(junction_path + "settings.json"):
        filename = "settings.json"
        src = str(python_src_dir) + "/settings/" + filename
        dst = str(junction_path) + filename
        copyfile(src, dst)
    return read_json_file(junction_path + "settings.json")


def get_settings_as_str():
    set_d = get_settings()
    set_str = ""
    for k, v in set_d.items():
        set_str += f"{k}: {v}\n"
    return set_str


### Flask


def flash_success(msg):
    flash(msg, "success")


def flash_error(msg):
    flash(msg, "danger")


###  Currency conversions

COIN_PER_SAT = Decimal(10) ** -8
SAT_PER_COIN = 100_000_000


def btc_to_sat(btc):
    return int(btc * SAT_PER_COIN)


def sat_to_btc(sat):
    return Decimal(sat / 100_000_000).quantize(COIN_PER_SAT)


### RPC


class RPC:
    wallet_template = "http://{rpc_username}:{rpc_password}@{rpc_host}:{rpc_port}/wallet/{wallet_name}"

    def __init__(self, wallet_name="", settings=None):
        if settings is None:
            settings = get_settings()
        self.uri = self.wallet_template.format(**settings, wallet_name=wallet_name)

    def __getattr__(self, name):
        """Create new proxy for every call to prevent timeouts"""
        rpc = AuthServiceProxy(self.uri, timeout=60)  # 1 minute timeout
        return getattr(rpc, name)


def test_rpc(settings):
    rpc = RPC(settings=settings)
    try:
        rpc.getblockchaininfo()
        return True
    except:
        return False


### ColdCard

# FIXME: do this with hwilib.devices.coldcard
# `real_file_upload` is the only thing that's missing
from ckcc.cli import ColdcardDevice, real_file_upload, MAX_BLK_LEN, CCProtocolPacker
from io import BytesIO

multisig_header = """Name: {name}
Policy: {m} of {n}
Derivation: {path}
Format: {format}

"""
multisig_key = "\n{fingerprint}: {xpub}"


def coldcard_multisig_file(wallet):
    name = wallet.name[:20]  # 20 character max
    contents = multisig_header.format(
        name=name, m=wallet.m, n=wallet.n, path="m/44'/1'/0'", format="P2SH"
    )
    for signer in wallet.signers:
        contents += multisig_key.format(
            fingerprint=signer["fingerprint"], xpub=signer["xpub"]
        )

    return BytesIO(contents.encode())


def coldcard_enroll(wallet):
    multisig_file = coldcard_multisig_file(wallet)

    force_serial = None
    dev = ColdcardDevice(sn=force_serial)

    file_len, sha = real_file_upload(multisig_file, MAX_BLK_LEN, dev=dev)

    dev.send_recv(CCProtocolPacker.multisig_enroll(file_len, sha))
