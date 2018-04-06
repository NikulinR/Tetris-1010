# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1010.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys,random
from PyQt5 import QtCore, QtGui, QtWidgets


class Figure():
    
    def __init__(self, shape):        
        self.shape = shape
        self.__size = [len(shape),len(shape[0])]
    
    @staticmethod
    def spinfigure(self):
        self = Figure(list(zip(*self.shape)))
        return self
        
    @property
    def size(self):                       # Чтение
        return self.__size
        
        

class Game():
        
    __score = 0
    __setfig = []
    def __init__(self, height, width):
        self.__cellfield=[]        
        self.height = height
        self.width = width   
        for i in range(height):
            self.__cellfield.append([0 for i in range(width)])  
        self.__get_figures_fromfile__("Shapes.txt")
    
    def __get_figures_fromfile__(self,path):
        blocks = []
        f = open(path, 'r')
        unparsed = f.read()
        unparsed = unparsed.split('\n-\n')
        for fig in unparsed:
            blocks.append([i.split(' ') for i in fig.split('\n')])
        for fig in blocks:
            self.__setfig.append(Figure(fig))
            
    def placefigure(self, x, y, fig):
        if ((x+fig.size[1]) <= self.width) & ((y+fig.size[0]) <= self.height):
            for i in range(fig.size[0]):
                for j in range(fig.size[1]):
                    if (int(self.__cellfield[y+i][x+j]) + int(fig.shape[i][j]))>1:
                        return
            for i in range(fig.size[0]):
                for j in range(fig.size[1]):
                    self.__cellfield[y+i][x+j] = fig.shape[i][j]
                    
    def givefig(self):
        if random.getrandbits(1):
            return random.choice(self.__setfig)
        else:
            return Figure.spinfigure(random.choice(self.__setfig))
    
    def invalidate(self):
        fullx = []
        fully = []
        flipfield = list(zip(*self.__cellfield))
        
        for i in range(len(self.__cellfield)):
            isfullx = False
            if 0 not in self.__cellfield[i]:
                isfullx = True
            if isfullx:
                fullx.append(i) 
        
        for i in range(len(flipfield)):
            isfully = False
            if 0 not in flipfield[i]:
                isfully = True
            if isfully:
                fully.append(i)
        
        for win in fullx:
            self.__cellfield[win] = [0]*self.width
            self.__score+=self.width
            
        for win in fully:
            flipfield[win] = [0]*self.height
            self.__cellfield = list(zip(*flipfield))
            self.__score+=self.height
    
    @property
    def field(self):                       # Чтение
        return self.__cellfield
    
    @property
    def score(self):                       # Чтение
        return self.__score
    
    @field.setter
    def field(self, value):                # Запись
        self.__cellfield = value
    
    @field.deleter
    def field(self):
        self.__cellfield = []              # Удаление
        for i in range(self.height):
            self.__cellfield.append([0 for i in range(self.width)])


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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() 
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) 
    MainWindow.show() 
    sys.exit(app.exec_())
    
  