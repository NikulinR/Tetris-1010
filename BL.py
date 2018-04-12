# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
"""
1. UI
2. connect UI and Game
3. mousemove
"""

import random


class Figure():
    
    def __init__(self, shape):        
        self.shape = shape
        self.__size = [len(shape),len(shape[0])]
    
    @staticmethod
    def spinfigure(self):
        self = Figure(list(map(list, zip(*self.shape))))
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
            self.__cellfield.append(list(0 for i in range(width)))  
        self.__get_figures_fromfile__("Resourses/Shapes.txt")
        
            
        
        
    
    def __get_figures_fromfile__(self,path):
        blocks = []
        f = open(path, 'r')
        unparsed = f.read()
        unparsed = unparsed.split('\n-\n')
        for fig in unparsed:
            blocks.append(list(i.split(' ') for i in fig.split('\n')))
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
                    self.__cellfield[y+i][x+j] = int(self.__cellfield[y+i][x+j]) + int(fig.shape[i][j]) 
                    
    def givefig(self):
        if random.getrandbits(1):
            return random.choice(self.__setfig)
        else:
            return Figure.spinfigure(random.choice(self.__setfig))
    
    def invalidate(self):
        fullx = []
        fully = []
        flipfield = list(map(list, zip(*self.__cellfield)))
        
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
        
            
        for win in fully:
            flipfield[win] = [0]*self.height            
            self.__score+=self.height
        
        self.__cellfield = list(map(list, zip(*flipfield)))
        
        for win in fullx:
            self.__cellfield[win] = [0]*self.width
            self.__score+=self.width
    
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
            self.__cellfield.append(list(0 for i in range(self.width)))  