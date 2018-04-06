import sys
import BL,MainFormDesigner, SettingsDesigner
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QFont
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
        
    def setOption_Clicked(self):
        self.lable.setText("RUNNED")
        self.setting = optionsForm()
        self.setting.show()     
    
    def btnRun_Clicked(self):
        self.game = BL.Game(height, width)        
        self.fig1 = self.game.givefig().shape
        self.fig2 = self.game.givefig().shape
        self.fig3 = self.game.givefig().shape
        
class optionsForm(QMainWindow, SettingsDesigner.Ui_QSettings):
    
    def __init__(self):        
        super().__init__()
        self.setupUi(self)
        self.sliderHeight.valueChanged.connect(self.lcdHeight.display)
        self.sliderWidth.valueChanged.connect(self.lcdWidth.display)
        
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = mainForm()
    form.show()
    app.exec()