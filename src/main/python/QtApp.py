#!/usr/bin/env python
import json
from pathlib import Path

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDial,
    QDialog,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QScrollBar,
    QSizePolicy,
    QSlider,
    QSpinBox,
    QStyleFactory,
    QTableWidget,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

import sys

from hwilib import commands

wallets = commands.enumerate()
wallet_list = [wallet["type"] for wallet in wallets]

here = Path(__file__).parent
main_folder = Path(here).parent


class Junction(QDialog):
    def __init__(self, parent=None):
        super(Junction, self).__init__(parent)

        self.originalPalette = QApplication.palette()
        self.create_wallet_form()
        self.create_rpc_settings_form()
        self.create_main_tab_widget()

        main_layout = QGridLayout()
        main_layout.addWidget(self.main_tab_widget, 1, 0)
        main_layout.setRowStretch(1, 2)
        main_layout.setRowStretch(2, 2)
        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 1)
        self.setLayout(main_layout)

        self.setWindowTitle("Hardware Wallet Junction")
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        QApplication.setPalette(QApplication.style().standardPalette())

    def create_main_tab_widget(self):
        self.main_tab_widget = QTabWidget()
        self.main_tab_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)

        tab1 = self.rpc_settings_form
        tab2 = self.wallet_form
        self.main_tab_widget.addTab(tab1, "RPC Settings")
        self.main_tab_widget.addTab(tab2, "Create Wallet")

    def create_rpc_settings_form(self):
        self.rpc_settings_form = QGroupBox("Configure testnet RPC parameters")
        self.rpc_user = QLineEdit()
        self.rpc_pw = QLineEdit()
        self.rpc_pw.setEchoMode(QLineEdit.Password)
        self.rpc_host = QLineEdit()
        self.rpc_host.setText("127.0.0.1")
        self.rpc_port = QLineEdit()
        self.rpc_port.setText("18332")
        self.rpc_save_btn = QPushButton("Save")
        self.rpc_save_btn.clicked.connect(lambda: self.update_conf())

        layout = QFormLayout()
        layout.addRow(QLabel("RPC Username:"), self.rpc_user)
        layout.addRow(QLabel("RPC Password:"), self.rpc_pw)
        layout.addRow(QLabel("RPC Host:"), self.rpc_host)
        layout.addRow(QLabel("RPC Port:"), self.rpc_port)
        layout.addWidget(self.rpc_save_btn)
        self.rpc_settings_form.setLayout(layout)

    def create_wallet_form(self):
        self.wallet_form = QGroupBox("Create a new wallet")
        sig_req = QLineEdit()
        sig_req.setText("2")
        total_sig = QLineEdit()
        total_sig.setText("3")
        layout = QFormLayout()
        layout.addRow(QLabel("Wallet name:"), QLineEdit())
        layout.addRow(QLabel("Signatures required:"), sig_req)
        layout.addRow(QLabel("Total signers:"), total_sig)
        self.wallet_form.setLayout(layout)

    def update_conf(self):
        with open(main_folder/"settings/settings.json") as settings:
            data = json.load(settings)
        data["rpc_username"] = self.rpc_user.text()
        data["rpc_password"] = self.rpc_pw.text()
        data["rpc_host"] = self.rpc_host.text()
        data["rpc_port"] = self.rpc_port.text()
        with open(main_folder/"settings/settings.json", "w") as outfile:
            json.dump(data, outfile, indent=4)


if __name__ == "__main__":
    appctxt = ApplicationContext()
    hwi_interface = Junction()
    hwi_interface.resize(500, 500)
    hwi_interface.show()
    sys.exit(appctxt.app.exec_())
