import sys
import BL,MainFormDesigner, SettingsDesigner
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFrame
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap, QPen
from PyQt5.QtCore import Qt
"""Реализовать отрисовку матриц в функции!"""

height = 10
width = 10    


class mainForm(QMainWindow, MainFormDesigner.Ui_MainWindow):
    
    def __init__(self):        
        super().__init__()
        self.setupUi(self)
        self.setOptions.clicked.connect(self.setOption_Clicked)        
        self.btnRun.clicked.connect(self.btnRun_Clicked)
        self.pix = QPixmap(self.setfig1.height(),self.setfig1.width())
        self.pix.fill(QColor(0,0,0,0))        

    
    def setOption_Clicked(self):
        self.setting = optionsForm()
        self.setting.show()     
    
    def btnRun_Clicked(self):
        self.game = BL.Game(height, width)
        
        
    
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