# -*- coding: utf-8 -*-
import random
from PyQt5.QtGui import QColor

class Figure():
    def __init__(self, x, y, color, choisen):
        self.x = x
        self.y = y
        self.choisen = choisen
        self.color = color
       
class Field():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.list_field = []
        self.list_color = [QColor.green, QColor.yellow, QColor.red]
        
        for i in range(height):
            tmp = []
            for j in range(width):
                  tmp.append(Figure(i, j, random.choice(self.list_color), True))
            self.list_field.append(tmp)
            
            
    def DeleteShape(self):
        tmp = []
        for i in range(self.height):
            for j in range(self.width):
                if self.list_field[i][j].choisen == True:
                    tmp.append([i,j])
        for i in range(len(tmp)):
            for j in range(len(self.list_field[tmp[i][0]]), 0, -1):
                print(i, j)
                if j == tmp[i][1]:
                    del self.list_field[tmp[i][0]][j]
                    
        self.height = len(self.list_field)
        if self.height > 0: 
            self.width = len(self.list_field[0]) 
        else:
            self.width = 0            
                
                                
    def OutConsole(self):
        string_color = ""
        for i in range(self.height):
            for j in range(self.width):
                if self.list_field[i][j].color == QColor.green:
                    string_color += " G "
                if self.list_field[i][j].color == QColor.yellow:
                    string_color += " Y "
                if self.list_field[i][j].color == QColor.red:
                    string_color += " R "
            string_color += "\n"
        print(string_color)
                
pole = Field(5,5)
pole.DeleteShape()
pole.OutConsole()

    
#def ChoisenUnit():
    
            
#def ChoisenShape():
            
    
    