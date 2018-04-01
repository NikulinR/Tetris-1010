# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""

import sys, random

from PyQt5.QtWidgets import QApplication, QWidget

class Window(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.show()

class Figure():
    
    def __init__(self, shape):        
        self.shape = shape
        self.__size = [len(shape),len(shape[0])]
    
    """def spinfigure(self):
        self.shape = list(zip(self.shape))
        self.__size = self.__size.reverse()
        return self"""
        
    @property
    def size(self):                       # Чтение
        return self.__size
        
        

class Game():
        
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
        if ((x+fig.size[1]) < self.width) & ((y+fig.size[0]) < self.height):
            for i in range(fig.size[0]):
                for j in range(fig.size[1]):
                    self.__cellfield[y+i][x+j] = fig.shape[i][j]
                    
    def givefig(self):
        return random.choice(self.__setfig)
    
    @property
    def field(self):                       # Чтение
        return self.__cellfield
    
    @field.setter
    def field(self, value):                # Запись
        self.__cellfield = value
    
    @field.deleter
    def field(self):
        self.__cellfield = []              # Удаление
        for i in range(self.height):
            self.__cellfield.append([0 for i in range(self.width)])  
    
        
           
f = Game(10,10)
f.placefigure(0,0,f.givefig())
print(f.field)

"""if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())"""