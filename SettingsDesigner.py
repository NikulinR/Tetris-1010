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
        icon = QtGui.QIcon("Resourses/set.png")
        QSettings.setWindowIcon(icon)
        
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
        
        self.lW = QtWidgets.QLabel(self.centralwidget)
        self.lW.setObjectName("lW")
        self.lW.setGeometry(QtCore.QRect(60, 40, 51, 20))
        font=QtGui.QFont()
        font.setPointSize(16)
        self.lW.setFont(font)
        self.lH = QtWidgets.QLabel(self.centralwidget)
        self.lH.setObjectName("lH")
        self.lH.setGeometry(QtCore.QRect(60, 70, 51, 20))
        self.lH.setFont(font)
        
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
        
        self.lH.setText(_translate("QSettings", "10"))
        self.lW.setText(_translate("QSettings", "10"))

