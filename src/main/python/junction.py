# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'junction.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Junction(object):
    def setupUi(self, Junction):
        Junction.setObjectName("Junction")
        Junction.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Junction.sizePolicy().hasHeightForWidth())
        Junction.setSizePolicy(sizePolicy)
        Junction.setMinimumSize(QtCore.QSize(640, 480))
        self.centralWidget = QtWidgets.QWidget(Junction)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainTab = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainTab.sizePolicy().hasHeightForWidth())
        self.mainTab.setSizePolicy(sizePolicy)
        self.mainTab.setToolTip("")
        self.mainTab.setStatusTip("")
        self.mainTab.setWhatsThis("")
        self.mainTab.setAccessibleName("")
        self.mainTab.setAccessibleDescription("")
        self.mainTab.setObjectName("mainTab")
        self.Wallet = QtWidgets.QWidget()
        self.Wallet.setStatusTip("")
        self.Wallet.setWhatsThis("")
        self.Wallet.setAccessibleName("")
        self.Wallet.setAccessibleDescription("")
        self.Wallet.setObjectName("Wallet")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Wallet)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.walletWidget = QtWidgets.QWidget(self.Wallet)
        self.walletWidget.setToolTip("")
        self.walletWidget.setStatusTip("")
        self.walletWidget.setWhatsThis("")
        self.walletWidget.setAccessibleName("")
        self.walletWidget.setAccessibleDescription("")
        self.walletWidget.setObjectName("walletWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.walletWidget)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.walletNameLabel = QtWidgets.QLabel(self.walletWidget)
        self.walletNameLabel.setToolTip("")
        self.walletNameLabel.setStatusTip("")
        self.walletNameLabel.setWhatsThis("")
        self.walletNameLabel.setAccessibleName("")
        self.walletNameLabel.setAccessibleDescription("")
        self.walletNameLabel.setObjectName("walletNameLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.walletNameLabel)
        self.walletNameLineEdit = QtWidgets.QLineEdit(self.walletWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.walletNameLineEdit.sizePolicy().hasHeightForWidth())
        self.walletNameLineEdit.setSizePolicy(sizePolicy)
        self.walletNameLineEdit.setToolTip("")
        self.walletNameLineEdit.setStatusTip("")
        self.walletNameLineEdit.setWhatsThis("")
        self.walletNameLineEdit.setAccessibleName("")
        self.walletNameLineEdit.setAccessibleDescription("")
        self.walletNameLineEdit.setPlaceholderText("e.g. 2-of-3 cc trezor ledger")
        self.walletNameLineEdit.setObjectName("walletNameLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.walletNameLineEdit)
        self.requiredSignersLabel = QtWidgets.QLabel(self.walletWidget)
        self.requiredSignersLabel.setToolTip("")
        self.requiredSignersLabel.setStatusTip("")
        self.requiredSignersLabel.setWhatsThis("")
        self.requiredSignersLabel.setAccessibleName("")
        self.requiredSignersLabel.setAccessibleDescription("")
        self.requiredSignersLabel.setObjectName("requiredSignersLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.requiredSignersLabel)
        self.requiredSignersLineEdit = QtWidgets.QLineEdit(self.walletWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requiredSignersLineEdit.sizePolicy().hasHeightForWidth())
        self.requiredSignersLineEdit.setSizePolicy(sizePolicy)
        self.requiredSignersLineEdit.setToolTip("")
        self.requiredSignersLineEdit.setStatusTip("")
        self.requiredSignersLineEdit.setWhatsThis("")
        self.requiredSignersLineEdit.setAccessibleName("")
        self.requiredSignersLineEdit.setAccessibleDescription("")
        self.requiredSignersLineEdit.setPlaceholderText("")
        self.requiredSignersLineEdit.setObjectName("requiredSignersLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.requiredSignersLineEdit)
        self.totalSignersLabel = QtWidgets.QLabel(self.walletWidget)
        self.totalSignersLabel.setToolTip("")
        self.totalSignersLabel.setStatusTip("")
        self.totalSignersLabel.setWhatsThis("")
        self.totalSignersLabel.setAccessibleName("")
        self.totalSignersLabel.setAccessibleDescription("")
        self.totalSignersLabel.setObjectName("totalSignersLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.totalSignersLabel)
        self.totalSignersLineEdit = QtWidgets.QLineEdit(self.walletWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalSignersLineEdit.sizePolicy().hasHeightForWidth())
        self.totalSignersLineEdit.setSizePolicy(sizePolicy)
        self.totalSignersLineEdit.setToolTip("")
        self.totalSignersLineEdit.setStatusTip("")
        self.totalSignersLineEdit.setWhatsThis("")
        self.totalSignersLineEdit.setAccessibleName("")
        self.totalSignersLineEdit.setAccessibleDescription("")
        self.totalSignersLineEdit.setPlaceholderText("")
        self.totalSignersLineEdit.setObjectName("totalSignersLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.totalSignersLineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.walletWidget)
        self.buttonBox.setToolTip("")
        self.buttonBox.setStatusTip("")
        self.buttonBox.setWhatsThis("")
        self.buttonBox.setAccessibleName("")
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.verticalLayout_3.addWidget(self.walletWidget)
        self.mainTab.addTab(self.Wallet, "")
        self.Devices = QtWidgets.QWidget()
        self.Devices.setStatusTip("")
        self.Devices.setWhatsThis("")
        self.Devices.setAccessibleName("")
        self.Devices.setAccessibleDescription("")
        self.Devices.setObjectName("Devices")
        self.mainTab.addTab(self.Devices, "")
        self.Settings = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Settings.sizePolicy().hasHeightForWidth())
        self.Settings.setSizePolicy(sizePolicy)
        self.Settings.setStatusTip("")
        self.Settings.setWhatsThis("")
        self.Settings.setAccessibleName("")
        self.Settings.setAccessibleDescription("")
        self.Settings.setObjectName("Settings")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Settings)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rPCSettingsWidget = QtWidgets.QWidget(self.Settings)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rPCSettingsWidget.sizePolicy().hasHeightForWidth())
        self.rPCSettingsWidget.setSizePolicy(sizePolicy)
        self.rPCSettingsWidget.setObjectName("rPCSettingsWidget")
        self.formLayout = QtWidgets.QFormLayout(self.rPCSettingsWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.rPCUsernameLabel = QtWidgets.QLabel(self.rPCSettingsWidget)
        self.rPCUsernameLabel.setToolTip("")
        self.rPCUsernameLabel.setStatusTip("")
        self.rPCUsernameLabel.setWhatsThis("")
        self.rPCUsernameLabel.setAccessibleName("")
        self.rPCUsernameLabel.setAccessibleDescription("")
        self.rPCUsernameLabel.setText("RPC Username")
        self.rPCUsernameLabel.setObjectName("rPCUsernameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rPCUsernameLabel)
        self.rPCUsernameLineEdit = QtWidgets.QLineEdit(self.rPCSettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rPCUsernameLineEdit.sizePolicy().hasHeightForWidth())
        self.rPCUsernameLineEdit.setSizePolicy(sizePolicy)
        self.rPCUsernameLineEdit.setToolTip("")
        self.rPCUsernameLineEdit.setStatusTip("")
        self.rPCUsernameLineEdit.setWhatsThis("")
        self.rPCUsernameLineEdit.setAccessibleName("")
        self.rPCUsernameLineEdit.setAccessibleDescription("")
        self.rPCUsernameLineEdit.setPlaceholderText("")
        self.rPCUsernameLineEdit.setObjectName("rPCUsernameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rPCUsernameLineEdit)
        self.rPCPasswordLabel = QtWidgets.QLabel(self.rPCSettingsWidget)
        self.rPCPasswordLabel.setToolTip("")
        self.rPCPasswordLabel.setStatusTip("")
        self.rPCPasswordLabel.setWhatsThis("")
        self.rPCPasswordLabel.setAccessibleName("")
        self.rPCPasswordLabel.setAccessibleDescription("")
        self.rPCPasswordLabel.setText("RPC Password")
        self.rPCPasswordLabel.setObjectName("rPCPasswordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rPCPasswordLabel)
        self.rPCPasswordLineEdit = QtWidgets.QLineEdit(self.rPCSettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rPCPasswordLineEdit.sizePolicy().hasHeightForWidth())
        self.rPCPasswordLineEdit.setSizePolicy(sizePolicy)
        self.rPCPasswordLineEdit.setToolTip("")
        self.rPCPasswordLineEdit.setStatusTip("")
        self.rPCPasswordLineEdit.setWhatsThis("")
        self.rPCPasswordLineEdit.setAccessibleName("")
        self.rPCPasswordLineEdit.setAccessibleDescription("")
        self.rPCPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.rPCPasswordLineEdit.setPlaceholderText("")
        self.rPCPasswordLineEdit.setObjectName("rPCPasswordLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rPCPasswordLineEdit)
        self.rPCHostLabel = QtWidgets.QLabel(self.rPCSettingsWidget)
        self.rPCHostLabel.setToolTip("")
        self.rPCHostLabel.setStatusTip("")
        self.rPCHostLabel.setWhatsThis("")
        self.rPCHostLabel.setAccessibleName("")
        self.rPCHostLabel.setAccessibleDescription("")
        self.rPCHostLabel.setText("RPC Host")
        self.rPCHostLabel.setObjectName("rPCHostLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rPCHostLabel)
        self.rPCHostLineEdit = QtWidgets.QLineEdit(self.rPCSettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rPCHostLineEdit.sizePolicy().hasHeightForWidth())
        self.rPCHostLineEdit.setSizePolicy(sizePolicy)
        self.rPCHostLineEdit.setToolTip("")
        self.rPCHostLineEdit.setStatusTip("")
        self.rPCHostLineEdit.setWhatsThis("")
        self.rPCHostLineEdit.setAccessibleName("")
        self.rPCHostLineEdit.setAccessibleDescription("")
        self.rPCHostLineEdit.setPlaceholderText("")
        self.rPCHostLineEdit.setObjectName("rPCHostLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rPCHostLineEdit)
        self.rPCPortLabel = QtWidgets.QLabel(self.rPCSettingsWidget)
        self.rPCPortLabel.setToolTip("")
        self.rPCPortLabel.setStatusTip("")
        self.rPCPortLabel.setWhatsThis("")
        self.rPCPortLabel.setAccessibleName("")
        self.rPCPortLabel.setAccessibleDescription("")
        self.rPCPortLabel.setText("RPC Port")
        self.rPCPortLabel.setObjectName("rPCPortLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.rPCPortLabel)
        self.rPCPortLineEdit = QtWidgets.QLineEdit(self.rPCSettingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rPCPortLineEdit.sizePolicy().hasHeightForWidth())
        self.rPCPortLineEdit.setSizePolicy(sizePolicy)
        self.rPCPortLineEdit.setToolTip("")
        self.rPCPortLineEdit.setStatusTip("")
        self.rPCPortLineEdit.setWhatsThis("")
        self.rPCPortLineEdit.setAccessibleName("")
        self.rPCPortLineEdit.setAccessibleDescription("")
        self.rPCPortLineEdit.setPlaceholderText("")
        self.rPCPortLineEdit.setObjectName("rPCPortLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rPCPortLineEdit)
        self.RPCSettingsDialog = QtWidgets.QDialogButtonBox(self.rPCSettingsWidget)
        self.RPCSettingsDialog.setToolTip("")
        self.RPCSettingsDialog.setStatusTip("")
        self.RPCSettingsDialog.setWhatsThis("")
        self.RPCSettingsDialog.setAccessibleName("")
        self.RPCSettingsDialog.setAccessibleDescription("")
        self.RPCSettingsDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RPCSettingsDialog.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.RPCSettingsDialog.setObjectName("RPCSettingsDialog")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.RPCSettingsDialog)
        self.verticalLayout_2.addWidget(self.rPCSettingsWidget)
        self.currentRPCSettingsLabel = QtWidgets.QLabel(self.Settings)
        self.currentRPCSettingsLabel.setToolTip("")
        self.currentRPCSettingsLabel.setStatusTip("")
        self.currentRPCSettingsLabel.setWhatsThis("")
        self.currentRPCSettingsLabel.setText("    Current RPC settings as read from file:")
        self.currentRPCSettingsLabel.setObjectName("currentRPCSettingsLabel")
        self.verticalLayout_2.addWidget(self.currentRPCSettingsLabel)
        self.currentRPCSettingsWidget = QtWidgets.QWidget(self.Settings)
        self.currentRPCSettingsWidget.setObjectName("currentRPCSettingsWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.currentRPCSettingsWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.currentRPCSettingsTextBrowser = QtWidgets.QTextBrowser(self.currentRPCSettingsWidget)
        self.currentRPCSettingsTextBrowser.setToolTip("")
        self.currentRPCSettingsTextBrowser.setStatusTip("")
        self.currentRPCSettingsTextBrowser.setWhatsThis("")
        self.currentRPCSettingsTextBrowser.setAccessibleName("")
        self.currentRPCSettingsTextBrowser.setAccessibleDescription("")
        self.currentRPCSettingsTextBrowser.setPlaceholderText("")
        self.currentRPCSettingsTextBrowser.setObjectName("currentRPCSettingsTextBrowser")
        self.horizontalLayout.addWidget(self.currentRPCSettingsTextBrowser)
        spacerItem = QtWidgets.QSpacerItem(265, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.currentRPCSettingsWidget)
        self.mainTab.addTab(self.Settings, "Settings")
        self.verticalLayout.addWidget(self.mainTab)
        Junction.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Junction)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menuBar.setObjectName("menuBar")
        Junction.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(Junction)
        self.mainToolBar.setObjectName("mainToolBar")
        Junction.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(Junction)
        self.statusBar.setObjectName("statusBar")
        Junction.setStatusBar(self.statusBar)

        self.retranslateUi(Junction)
        self.mainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Junction)

    def retranslateUi(self, Junction):
        _translate = QtCore.QCoreApplication.translate
        Junction.setWindowTitle(_translate("Junction", "Junction"))
        self.walletNameLabel.setText(_translate("Junction", "Wallet name"))
        self.requiredSignersLabel.setText(_translate("Junction", "Required Signers"))
        self.totalSignersLabel.setText(_translate("Junction", "Total Signers"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.Wallet), _translate("Junction", "Wallet"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.Devices), _translate("Junction", "Devices"))
        self.rPCHostLineEdit.setText(_translate("Junction", "127.0.0.1"))
        self.rPCPortLineEdit.setText(_translate("Junction", "18332"))
