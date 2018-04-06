import sys
import BL,MainFormDesigner, SettingsDesigner
from PyQt5 import QtGui,QtCore,QtWidgets


class mainForm(QtWidgets.QMainWindow, MainFormDesigner.Ui_MainWindow):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow() 
    #SettingsWindow = QtWidgets.QMainWindow()
    
    mainui = MainFormDesigner.Ui_MainWindow()
    mainui.setupUi(MainWindow) 
    
    #uiset = sett.Ui_QSettings()
    #uiset.setupUi(SettingsWindow)
    
    #SettingsWindow.show()
    MainWindow.show() 
    sys.exit(app.exec_())