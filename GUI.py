import sys,random
import BL,MainFormDesigner, SettingsDesigner
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFrame
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap, QPen
from PyQt5.QtCore import Qt, QRect
"""Реализовать отрисовку матриц в функции!"""

height = 10
width = 10    


class mainForm(QMainWindow, MainFormDesigner.Ui_MainWindow):
    
    def __init__(self):        
        super().__init__()
        self.setupUi(self)
        self.setOptions.clicked.connect(self.setOption_Clicked)        
        self.btnRun.clicked.connect(self.btnRun_Clicked)
        self.pixset1 = QPixmap(self.setfig1.height(),self.setfig1.width())
        self.pixset1.fill(QColor(0,0,0,0))      
        self.pixset2 = QPixmap(self.setfig2.height(),self.setfig2.width())
        self.pixset2.fill(QColor(0,0,0,0))  
        self.pixset3 = QPixmap(self.setfig3.height(),self.setfig3.width())
        self.pixset3.fill(QColor(0,0,0,0))  
        self.pixfield = QPixmap(self.field.width(),self.field.height())
        self.pixfield.fill(QColor(0,0,0,0)) 
        self.tmppixfield = QPixmap(self.field.width(),self.field.height())
        self.tmppixfield.fill(QColor(0,0,0,0)) 

    
    def setOption_Clicked(self):
        self.setting = optionsForm()
        self.setting.show()     
    
    def btnRun_Clicked(self):
        self.game = BL.Game(height, width)
        p = QPainter(self)
        p.setBrush(QColor('green'))
        self.chosenFigure = None
        self.fig1 = self.game.givefig()
        self.fig2 = self.game.givefig()
        self.fig3 = self.game.givefig()
        self.counterfig = 3
        
        self.lScore.setText("start")
        self.color = QColor(random.randint(50,255),random.randint(50,255),random.randint(50,255))
        
        self.update()
    
    
    def mousePressEvent(self, e):        
        if e.button() == Qt.LeftButton:  
            if (self.setfig1.x() < e.x() < self.setfig1.x()+self.setfig1.width()) & (self.setfig1.y() < e.y() < self.setfig1.y()+self.setfig1.height()):
                #self.figid = 1
                self.chosenFigure = self.fig1
            if (self.setfig2.x() < e.x() < self.setfig2.x()+self.setfig2.width()) & (self.setfig2.y() < e.y() < self.setfig2.y()+self.setfig2.height()):
                #self.figid = 2
                self.chosenFigure = self.fig2
            if (self.setfig3.x() < e.x() < self.setfig3.x()+self.setfig3.width()) & (self.setfig3.y() < e.y() < self.setfig3.y()+self.setfig3.height()):
                #self.figid = 3
                self.chosenFigure = self.fig3
                
            
    def mouseMoveEvent(self, e):    
        self.tmppixfield.fill(Qt.white)
        p = QPainter(self)        
        sizex = self.tmppixfield.width()/width
        sizey = self.tmppixfield.height()/height
        i = int((e.x() - self.field.x())//(self.field.width()/width))
        j = int((e.y() - self.field.y())//(self.field.height()/height)) 
        for i in range(len(self.chosenFigure.shape)):
            for j in range(len(self.chosenFigure.shape[0])):                
                rect = QRect(j*sizex, i*sizey, sizex, sizey)                
                if (self.chosenFigure.shape[i][j] == 1):
                    p.fillRect(rect, self.color)
        p.drawPixmap(self.field.x(),self.field.y(),self.tmppixfield)

        
    def mouseReleaseEvent(self, e):
        if self.chosenFigure != None:
            if (self.field.x() < e.x() < self.field.x()+self.field.width()) & (self.field.y() < e.y() < self.field.y()+self.field.height()):   
                i = int((e.x() - self.field.x())//(self.field.width()/width))
                j = int((e.y() - self.field.y())//(self.field.height()/height))   
                self.lScore.setText(str((i,j)))
                self.game.field = self.game.placefigure(i,j,self.chosenFigure, self.game.field)
                self.counterfig -= 1
                if self.counterfig == 0:
                    self.fig1 = self.game.givefig()
                    self.fig2 = self.game.givefig()
                    self.fig3 = self.game.givefig()
                    self.counterfig = 3
        self.game.invalidate()
        self.lScore.setText(str(self.game.score))
        self.update()
        self.chosenFigure = None
        
    
        
    
    def paintEvent(self, e):
        p = QPainter(self)
        if self.fig1:
            self.drawFigure(self.fig1.shape, self.pixset1, self.color)
        if self.fig2:
            self.drawFigure(self.fig2.shape, self.pixset2, self.color)
        if self.fig3:
            self.drawFigure(self.fig3.shape, self.pixset3, self.color)
        if self.game:
            self.drawFigure(self.game.field, self.pixfield, self.color, w=width, h=height)
        
        p.drawPixmap(self.setfig1.x(),self.setfig1.y(),self.pixset1)
        p.drawPixmap(self.setfig2.x(),self.setfig2.y(),self.pixset2)
        p.drawPixmap(self.setfig3.x(),self.setfig3.y(),self.pixset3)
        p.drawPixmap(self.field.x(),self.field.y(),self.pixfield)
        
    def drawFigure(self, matr, bmap, color, w=5, h=5):
        bmap.fill(QColor(0,0,0,0))
        p = QPainter(bmap)
        
        sizex = bmap.width()/w
        sizey = bmap.height()/h
        for i in range(len(matr)):
            for j in range(len(matr[0])):                
                rect = QRect(j*sizex, i*sizey, sizex, sizey)                
                if (matr[i][j] == 1):                    
                    p.fillRect(rect, color)
                p.drawRect(rect)
        
    
class optionsForm(QMainWindow, SettingsDesigner.Ui_QSettings):
    
    def __init__(self):        
        super().__init__()
        self.setupUi(self)
        self.sliderHeight.valueChanged.connect(self.SetH)
        self.sliderWidth.valueChanged.connect(self.SetW)
        
    def SetH(self):
        global height
        height = self.sliderHeight.value()       
        self.lH.setText(str(self.sliderHeight.value()))
        
    def SetW(self):
        global width
        width = self.sliderWidth.value()     
        self.lW.setText(str(self.sliderWidth.value()))
        
    
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = mainForm()
    form.show()
    app.exec()