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

        styleComboBox = QComboBox()
        styleComboBox.addItems(wallet_list)

        styleLabel = QLabel("&Device:")
        styleLabel.setBuddy(styleComboBox)

        self.createRPCSettingsGroupBox()
        # self.createTopTabLayout()


        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.RPCSettingsGroupBox, 1, 0)
        mainLayout.setRowStretch(1, 2)
        mainLayout.setRowStretch(2, 2)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Hardware Wallet Junction")
        QApplication.setStyle(QStyleFactory.create("Fusion"))
        QApplication.setPalette(QApplication.style().standardPalette())

    def createTopTabLayout(self):
        self.topTabLayout = QTabWidget()
        self.topTabLayout.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Ignored
        )

        RPCSettings = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText(
            "Twinkle, twinkle, little star,\n"
            "How I wonder what you are.\n"
            "Up above the world so high,\n"
            "Like a diamond in the sky.\n"
            "Twinkle, twinkle, little star,\n"
            "How I wonder what you are!\n"
        )

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.topTabLayout.addTab(tab1, "&RPC Settings")
        self.topTabLayout.addTab(tab2, "Text &Edit")


    # def createTopLeftGroupBox(self):
    #     self.topLeftGroupBox = QGroupBox("Group 1")
    #
    #     radioButton1 = QRadioButton("Radio button 1")
    #     radioButton2 = QRadioButton("Radio button 2")
    #     radioButton3 = QRadioButton("Radio button 3")
    #     radioButton1.setChecked(True)
    #
    #     checkBox = QCheckBox("Tri-state check box")
    #     checkBox.setTristate(True)
    #     checkBox.setCheckState(Qt.PartiallyChecked)
    #
    #     layout = QVBoxLayout()
    #     layout.addWidget(radioButton1)
    #     layout.addWidget(radioButton2)
    #     layout.addWidget(radioButton3)
    #     layout.addWidget(checkBox)
    #     layout.addStretch(1)
    #     self.topLeftGroupBox.setLayout(layout)

    # def createTopRightGroupBox(self):
    #     self.topRightGroupBox = QGroupBox("Group 2")
    #
    #     defaultPushButton = QPushButton("Default Push Button")
    #     defaultPushButton.setDefault(True)
    #
    #     togglePushButton = QPushButton("Toggle Push Button")
    #     togglePushButton.setCheckable(True)
    #     togglePushButton.setChecked(True)
    #
    #     flatPushButton = QPushButton("Flat Push Button")
    #     flatPushButton.setFlat(True)
    #
    #     layout = QVBoxLayout()
    #     layout.addWidget(defaultPushButton)
    #     layout.addWidget(togglePushButton)
    #     layout.addWidget(flatPushButton)
    #     layout.addStretch(1)
    #     self.topRightGroupBox.setLayout(layout)



    def createRPCSettingsGroupBox(self):
        self.RPCSettingsGroupBox = QGroupBox("RPC Settings")

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


if __name__ == "__main__":
    appctxt = ApplicationContext()
    hwi_interface = Junction()
    hwi_interface.show()
    sys.exit(appctxt.app.exec_())
