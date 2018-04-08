import sys
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
        self.fig1 = None
        self.fig2 = None
        self.fig3 = None
        self.game = None
        self.chosenFigure = None
        self.counterfig = 3
        self.figid = None

    
    def setOption_Clicked(self):
        self.setting = optionsForm()
        self.setting.show()     
    
    def btnRun_Clicked(self):
        self.game = BL.Game(height, width)
        p = QPainter(self)
        p.setBrush(QColor('green'))
        self.fig1 = self.game.givefig()
        self.fig2 = self.game.givefig()
        self.fig3 = self.game.givefig()
        
        
        self.lScore.setText("start")
        
        
        self.update()
    
    
    def mousePressEvent(self, e):        
        if e.button() == Qt.LeftButton:  
            if (self.setfig1.x() < e.x() < self.setfig1.x()+self.setfig1.width()) & (self.setfig1.y() < e.y() < self.setfig1.y()+self.setfig1.height()):
                figid = 1
                self.chosenFigure = self.fig1
            if (self.setfig2.x() < e.x() < self.setfig2.x()+self.setfig2.width()) & (self.setfig2.y() < e.y() < self.setfig2.y()+self.setfig2.height()):
                figid = 2
                self.chosenFigure = self.fig2
            if (self.setfig3.x() < e.x() < self.setfig3.x()+self.setfig3.width()) & (self.setfig3.y() < e.y() < self.setfig3.y()+self.setfig3.height()):
                figid = 3
                self.chosenFigure = self.fig3
            else:
                figid = 0
                
            
    def mouseMoveEvent(self, e):
        pass
        
    def mouseReleaseEvent(self, e):
        if self.chosenFigure != None:
            if (self.field.x() < e.x() < self.field.x()+self.field.width()) & (self.field.y() < e.y() < self.field.y()+self.field.height()):   
                i = int((e.x() - self.field.x())//(self.field.width()/width))
                j = int((e.y() - self.field.y())//(self.field.height()/height))   
                self.lScore.setText(str((i,j)))
                self.game.placefigure(i,j,self.chosenFigure)
                self.counterfig -= 1
                if self.figid == 1:
                    self.fig1.shape = []
                if self.figid == 2:
                    self.fig2.shape = []
                if self.figid == 3:
                    self.fig3.shape = []
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
        
        self.drawFigure(self.fig1.shape, self.pixset1)
        self.drawFigure(self.fig2.shape, self.pixset2)
        self.drawFigure(self.fig3.shape, self.pixset3)
        self.drawFigure(self.game.field, self.pixfield, w=width, h=height)
        
        p.drawPixmap(self.setfig1.x(),self.setfig1.y(),self.pixset1)
        p.drawPixmap(self.setfig2.x(),self.setfig2.y(),self.pixset2)
        p.drawPixmap(self.setfig3.x(),self.setfig3.y(),self.pixset3)
        p.drawPixmap(self.field.x(),self.field.y(),self.pixfield)
        
    def drawFigure(self, matr, bmap=QPixmap, w=5, h=5):
        bmap.fill(QColor(0,0,0,0))
        p = QPainter(bmap)
        
        sizex = bmap.width()/w
        sizey = bmap.height()/h
        for i in range(len(matr)):
            for j in range(len(matr[0])):                
                rect = QRect(j*sizex, i*sizey, sizex, sizey)
                p.drawRect(rect)
                if matr[i][j] == '1':                    
                    p.fillRect(rect, Qt.red)
        
    
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