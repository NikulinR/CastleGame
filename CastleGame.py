# -*- coding: utf-8 -*-
import random
from PyQt5.QtGui import QColor

class Figure():
    def __init__(self, x, y, color, choisen):
        self.x = x
        self.y = y
        self.choisen = choisen
        self.color = color
    @property
    def Color(self):
        return self.color
       
class Field():
    
    score = 0
    
    @property
    def Score(self):
        return self.score
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.list_field = []
        self.list_color = [QColor.green, QColor.yellow, QColor.red]
        
        for i in range(height):
            tmp = []
            for j in range(width):
                  tmp.append(Figure(i, j, random.choice(self.list_color), False))
            self.list_field.append(tmp)
            
    def ChoisenUnit(self, i, j):
        self.list_field[i][j].choisen = True    
                        
    def DeleteShape(self):
        delindex = []
        for i in range(self.height):
            linedels = []
            for j in range(self.width):
                if self.list_field[i][j].choisen == True:
                    linedels.append(j)
            delindex.append([i, linedels])
                    
        for dind in delindex:
            tmpstr = []
            dels = 0
            for j in range(len(self.list_field[dind[0]])):
                if j not in dind[1]:                    
                    tmpstr.append(self.list_field[dind[0]][j])
                else:
                    dels+=1
                    self.score += 1
            self.list_field[dind[0]] = tmpstr
            for i in range(dels):
                self.list_field[dind[0]].append(Figure(i, j, random.choice(self.list_color), False))
                
                                
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
                if self.list_field[i][j].color == QColor.blue:
                    string_color += " B "
            string_color += "\n"
        print(string_color)
        
    def AddHuman(self):
        numRow = random.randint(0, self.height-1)
        numColHuman1 = random.randint(0, self.width//2-1)
        distance = 1 + random.randint(1, self.width//2-1)
        numColHuman2 = numColHuman1 + distance
         
        self.list_field[numRow][numColHuman1] = Figure(numRow, numColHuman1, QColor.blue, False)
        self.list_field[numRow][numColHuman2] = Figure(numRow, numColHuman2, QColor.blue, False)
        
    @staticmethod
    def GetNeighbourhood(i, j, list_field):
        arrayNeig = [list_field[i][j-1], list_field[i-1][j], list_field[i+1][j], list_field[i][j+1]]
        if i == 0:
            arrayNeig[1] = None
        if j == 0:
            arrayNeig[0] = None
        if  i == len(list_field)-1:
            arrayNeig[2] = None
        if  j == len(list_field[0])-1:
            arrayNeig[3] = None
        arrayNeig = list(filter(lambda x: x != None, arrayNeig))
        return arrayNeig
    
    def EndGame(self):
        arrayN = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.list_field[i][j].color == QColor.blue:
                    arrayN = self.GetNeighbourhood(i, j, self.list_field)
                    for i in range(len(arrayN)):
                        if arrayN[i].color == QColor.blue:
                            self.score += 1000
                            self.__init__(self.height, self.width)
                            self.AddHuman()  
       
"""pole = Field(5,5)
pole.OutConsole()
pole.ChoisenUnit(1, 0)
pole.DeleteShape()
pole.AddHuman()
pole.OutConsole()
print(pole.score)"""


    
            
    
    