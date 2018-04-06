# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QSettings(object):
    def setupUi(self, QSettings):
        QSettings.setObjectName("QSettings")
        QSettings.resize(221, 144)
        self.buttonBox = QtWidgets.QDialogButtonBox(QSettings)
        self.buttonBox.setGeometry(QtCore.QRect(10, 100, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.sliderWidth = QtWidgets.QSlider(QSettings)
        self.sliderWidth.setGeometry(QtCore.QRect(10, 10, 160, 22))
        self.sliderWidth.setMinimum(5)
        self.sliderWidth.setMaximum(30)
        self.sliderWidth.setOrientation(QtCore.Qt.Horizontal)
        self.sliderWidth.setObjectName("sliderWidth")
        self.lWidth = QtWidgets.QLabel(QSettings)
        self.lWidth.setGeometry(QtCore.QRect(20, 33, 81, 20))
        self.lWidth.setObjectName("lWidth")
        self.lcdWidth = QtWidgets.QLCDNumber(QSettings)
        self.lcdWidth.setGeometry(QtCore.QRect(110, 30, 61, 23))
        self.lcdWidth.setObjectName("lcdWidth")
        self.sliderHeight = QtWidgets.QSlider(QSettings)
        self.sliderHeight.setGeometry(QtCore.QRect(190, 10, 22, 111))
        self.sliderHeight.setMinimum(5)
        self.sliderHeight.setMaximum(30)
        self.sliderHeight.setOrientation(QtCore.Qt.Vertical)
        self.sliderHeight.setObjectName("sliderHeight")
        self.lHeight = QtWidgets.QLabel(QSettings)
        self.lHeight.setGeometry(QtCore.QRect(20, 72, 81, 21))
        self.lHeight.setObjectName("lHeight")
        self.lcdHeight = QtWidgets.QLCDNumber(QSettings)
        self.lcdHeight.setGeometry(QtCore.QRect(110, 70, 61, 23))
        self.lcdHeight.setObjectName("lcdHeight")

        self.retranslateUi(QSettings)
        self.buttonBox.accepted.connect(QSettings.accept)
        self.buttonBox.rejected.connect(QSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(QSettings)

    def retranslateUi(self, QSettings):
        _translate = QtCore.QCoreApplication.translate
        QSettings.setWindowTitle(_translate("QSettings", "Settings"))
        self.lWidth.setText(_translate("QSettings", "Width:"))
        self.lHeight.setText(_translate("QSettings", "Height: "))

