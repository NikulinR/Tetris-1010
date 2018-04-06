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
        QSettings.resize(226, 150)
        self.centralwidget = QtWidgets.QWidget(QSettings)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(10, 100, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lcdWidth = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdWidth.setGeometry(QtCore.QRect(110, 30, 61, 23))
        self.lcdWidth.setObjectName("lcdWidth")
        self.lcdHeight = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdHeight.setGeometry(QtCore.QRect(110, 70, 61, 23))
        self.lcdHeight.setObjectName("lcdHeight")
        self.lHeight = QtWidgets.QLabel(self.centralwidget)
        self.lHeight.setGeometry(QtCore.QRect(20, 72, 81, 21))
        self.lHeight.setObjectName("lHeight")
        self.sliderWidth = QtWidgets.QSlider(self.centralwidget)
        self.sliderWidth.setGeometry(QtCore.QRect(10, 10, 160, 22))
        self.sliderWidth.setMinimum(5)
        self.sliderWidth.setMaximum(30)
        self.sliderWidth.setOrientation(QtCore.Qt.Horizontal)
        self.sliderWidth.setObjectName("sliderWidth")
        self.sliderHeight = QtWidgets.QSlider(self.centralwidget)
        self.sliderHeight.setGeometry(QtCore.QRect(190, 10, 22, 111))
        self.sliderHeight.setMinimum(5)
        self.sliderHeight.setMaximum(30)
        self.sliderHeight.setOrientation(QtCore.Qt.Vertical)
        self.sliderHeight.setObjectName("sliderHeight")
        self.lWidth = QtWidgets.QLabel(self.centralwidget)
        self.lWidth.setGeometry(QtCore.QRect(20, 33, 81, 20))
        self.lWidth.setObjectName("lWidth")
        QSettings.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QSettings)
        self.statusbar.setObjectName("statusbar")
        QSettings.setStatusBar(self.statusbar)

        self.retranslateUi(QSettings)
        QtCore.QMetaObject.connectSlotsByName(QSettings)

    def retranslateUi(self, QSettings):
        _translate = QtCore.QCoreApplication.translate
        QSettings.setWindowTitle(_translate("QSettings", "Settings"))
        self.lHeight.setText(_translate("QSettings", "Height: "))
        self.lWidth.setText(_translate("QSettings", "Width:"))

