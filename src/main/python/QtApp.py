#!/usr/bin/env python

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDial,
    QDialog,
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


class Junction(QDialog):
    def __init__(self, parent=None):
        super(Junction, self).__init__(parent)

        self.originalPalette = QApplication.palette()
        self.createRPCSettingsGroupBox()
        self.createWalletGroupBox()
        self.createMainTabWidget()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.mainTabWidget, 1, 0)
        mainLayout.setRowStretch(1, 2)
        mainLayout.setRowStretch(2, 2)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Hardware Wallet Junction")
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        QApplication.setPalette(QApplication.style().standardPalette())

    def createMainTabWidget(self):
        self.mainTabWidget = QTabWidget()
        self.mainTabWidget.setSizePolicy(QSizePolicy.Preferred,
                                         QSizePolicy.Ignored)

        tab1 = self.RPCSettingsGroupBox
        tab2 = self.WalletGroupBox
        self.mainTabWidget.addTab(tab1, "&RPC Settings")
        self.mainTabWidget.addTab(tab2, "Create Wallet")

    def createRPCSettingsGroupBox(self):
        self.RPCSettingsGroupBox = QGroupBox()

        RPCgroupLabel = QLabel("Configure testnet RPC parameters")


        RPCUsername = QLineEdit()
        RPCUsernameLabel = QLabel("&RPC Username:")
        RPCUsernameLabel.setBuddy(RPCUsername)

        RPCPassword = QLineEdit()
        RPCPassword.setEchoMode(QLineEdit.Password)
        RPCPasswordLabel = QLabel("&RPC Password:")
        RPCPasswordLabel.setBuddy(RPCUsername)

        RPCHost = QLineEdit()
        RPCHost.setText("127.0.0.1")
        RPCHostLabel = QLabel("&RPC Host:")
        RPCHostLabel.setBuddy(RPCHost)

        RPCPort = QLineEdit()
        RPCPortLabel = QLabel("&RPC Port:")
        RPCPort.setText("18332")
        RPCPortLabel.setBuddy(RPCPort)

        layout = QGridLayout()
        layout.addWidget(RPCgroupLabel,     0, 0, 1, 3)
        layout.addWidget(RPCUsernameLabel,  1, 0)
        layout.addWidget(RPCUsername,       1, 1, 1, 3)
        layout.addWidget(RPCPasswordLabel,  2, 0)
        layout.addWidget(RPCPassword,       2, 1, 1, 3)
        layout.addWidget(RPCHostLabel,      3, 0)
        layout.addWidget(RPCHost,           3, 1, 1, 3)
        layout.addWidget(RPCPortLabel,      4, 0)
        layout.addWidget(RPCPort,           4, 1, 1, 3)
        self.RPCSettingsGroupBox.setLayout(layout)

    def createWalletGroupBox(self):
        self.WalletGroupBox = QGroupBox()

        WalletgroupLabel = QLabel("Create a new multisig wallet")

        WalletName = QLineEdit()
        WalletNameLabel = QLabel("&Wallet name:")
        WalletNameLabel.setBuddy(WalletName)

        SignaturesReq = QLineEdit()
        SignaturesReq.setText("2")
        SignaturesReqLabel = QLabel("&Signatures Required:")
        SignaturesReqLabel.setBuddy(SignaturesReq)

        TotalSigners = QLineEdit()
        TotalSigners.setText("3")
        TotalSignersLabel = QLabel("&Total Signers:")
        TotalSignersLabel.setBuddy(TotalSigners)


        layout = QGridLayout()
        layout.addWidget(WalletgroupLabel,      0, 0, 1, 3)
        layout.addWidget(WalletNameLabel,       1, 0)
        layout.addWidget(WalletName,            1, 1, 1, 3)
        layout.addWidget(SignaturesReqLabel,    2, 0)
        layout.addWidget(SignaturesReq,         2, 1, 1, 3)
        layout.addWidget(TotalSignersLabel,     3, 0)
        layout.addWidget(TotalSigners,          3, 1, 1, 3)
        self.WalletGroupBox.setLayout(layout)


if __name__ == "__main__":
    appctxt = ApplicationContext()
    hwi_interface = Junction()
    hwi_interface.show()
    sys.exit(appctxt.app.exec_())
