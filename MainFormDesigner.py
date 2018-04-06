# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1010.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(727, 575))
        MainWindow.setMaximumSize(QtCore.QSize(727, 575))        
        icon = QtGui.QIcon("s1200.png")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdScore = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdScore.setGeometry(QtCore.QRect(590, 10, 131, 111)) 
        self.lcdScore.setSmallDecimalPoint(False)
        self.lcdScore.setObjectName("lcdScore")
        self.field = QtWidgets.QTableView(self.centralwidget)
        self.field.setGeometry(QtCore.QRect(10, 10, 561, 541))
        self.field.setFrameShape(QtWidgets.QFrame.Box)
        self.field.setFrameShadow(QtWidgets.QFrame.Raised)
        self.field.setObjectName("field")
        self.setfig1 = QtWidgets.QTableView(self.centralwidget)
        self.setfig1.setGeometry(QtCore.QRect(590, 140, 131, 131))
        self.setfig1.setFrameShape(QtWidgets.QFrame.Box)
        self.setfig1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setfig1.setObjectName("setfig1")
        self.setfig2 = QtWidgets.QTableView(self.centralwidget)
        self.setfig2.setGeometry(QtCore.QRect(590, 280, 131, 131))
        self.setfig2.setFrameShape(QtWidgets.QFrame.Box)
        self.setfig2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setfig2.setObjectName("setfig2")
        self.setfig3 = QtWidgets.QTableView(self.centralwidget)
        self.setfig3.setGeometry(QtCore.QRect(590, 420, 131, 131))
        self.setfig3.setFrameShape(QtWidgets.QFrame.Box)
        self.setfig3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setfig3.setObjectName("setfig3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuRules = QtWidgets.QMenu(self.menubar)
        self.menuRules.setObjectName("menuRules")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuRules.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "1010 Deluxe!"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuRules.setTitle(_translate("MainWindow", "Rules"))

    
  