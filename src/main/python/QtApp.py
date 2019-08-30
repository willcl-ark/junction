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


class Junction(QDialog):
    def __init__(self, parent=None):
        super(Junction, self).__init__(parent)

        self.originalPalette = QApplication.palette()
        self.createWalletForm()
        self.createRPCSettingsForm()
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
        self.mainTabWidget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)

        tab1 = self.RPCSettingsForm
        tab2 = self.WalletForm
        self.mainTabWidget.addTab(tab1, "RPC Settings")
        self.mainTabWidget.addTab(tab2, "Create Wallet")

    def createRPCSettingsForm(self):
        self.RPCSettingsForm = QGroupBox("Configure testnet RPC parameters")
        pw = QLineEdit()
        pw.setEchoMode(QLineEdit.Password)
        host = QLineEdit()
        host.setText("127.0.0.1")
        port = QLineEdit()
        port.setText("18332")
        layout = QFormLayout()
        layout.addRow(QLabel("RPC Username:"), QLineEdit())
        layout.addRow(QLabel("RPC Password:"), pw)
        layout.addRow(QLabel("RPC Host:"), host)
        layout.addRow(QLabel("RPC Port:"), port)
        self.RPCSettingsForm.setLayout(layout)

    def createWalletForm(self):
        self.WalletForm = QGroupBox("Create a new wallet")
        sig_req = QLineEdit()
        sig_req.setText("2")
        total_sig = QLineEdit()
        total_sig.setText("3")
        layout = QFormLayout()
        layout.addRow(QLabel("Wallet name:"), QLineEdit())
        layout.addRow(QLabel("Signatures required:"), sig_req)
        layout.addRow(QLabel("Total signers:"), total_sig)
        self.WalletForm.setLayout(layout)


if __name__ == "__main__":
    appctxt = ApplicationContext()
    hwi_interface = Junction()
    hwi_interface.show()
    sys.exit(appctxt.app.exec_())
