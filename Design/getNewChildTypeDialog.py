# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design/getNewChildTypeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(422, 176)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 4, 421, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.connectionTypeComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectionTypeComboBox.sizePolicy().hasHeightForWidth())
        self.connectionTypeComboBox.setSizePolicy(sizePolicy)
        self.connectionTypeComboBox.setCurrentText("")
        self.connectionTypeComboBox.setPlaceholderText("")
        self.connectionTypeComboBox.setObjectName("connectionTypeComboBox")
        self.gridLayout.addWidget(self.connectionTypeComboBox, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.chooseNewChildTypeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.chooseNewChildTypeButton.setObjectName("chooseNewChildTypeButton")
        self.gridLayout.addWidget(self.chooseNewChildTypeButton, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)
        self.childTypeComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.childTypeComboBox.sizePolicy().hasHeightForWidth())
        self.childTypeComboBox.setSizePolicy(sizePolicy)
        self.childTypeComboBox.setEditable(False)
        self.childTypeComboBox.setCurrentText("")
        self.childTypeComboBox.setPlaceholderText("")
        self.childTypeComboBox.setObjectName("childTypeComboBox")
        self.gridLayout.addWidget(self.childTypeComboBox, 1, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 4)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 4)
        self.gridLayout.setRowStretch(4, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.chooseNewChildTypeButton.setText(_translate("Dialog", "Create"))
        self.label.setText(_translate("Dialog", "Тип связи:"))
        self.label_2.setText(_translate("Dialog", "Тип дочернего элемента"))