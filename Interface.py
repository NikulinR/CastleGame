# -*- coding: utf-8 -*-

import sys,random, copy
import CastleGame, FormGame
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFrame
from PyQt5.QtGui import QPainter, QColor, QFont, QPixmap, QPen
from PyQt5.QtCore import Qt, QRect

class mainForm(QMainWindow, FormGame.Ui_MainWindow):
    
    def __init__(self):        
        super().__init__()
        self.setupUi(self)
        self.buttonRun.clicked.connect(self.buttonRun_Clicked)
        self.pixframe = QPixmap(self.frame.width(),self.frame.height())
        self.pixframe.fill(QColor(0,0,0,0))
        self.tmppixframe = QPixmap(self.frame.width(),self.frame.height())
        self.field = None
        self.moved = False
        ##############
        self.tmp_array = [] 
        self.numcho = 0
        ##############
    
    def buttonRun_Clicked(self):
        size = random.randint(10, 20)
        self.field = CastleGame.Field(size, size)
        self.field.AddHuman()
        self.update()
        
    #def mousePressEvent(self, e):
    
    def paintEvent(self, e):
        p = QPainter(self)
        
        if self.field:
            self.DrawField(self.pixframe)
            
        p.drawPixmap(self.frame.x(),self.frame.y(),self.pixframe)        
        
            
    def DrawField(self, pixmap):        
        pixmap.fill(QColor(0,0,0,0))
        p = QPainter(pixmap)
        matrix = self.field.list_field
        
        #размер клетки
        sizex = pixmap.width()/len(matrix[0])
        sizey = pixmap.height()/len(matrix)   
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):                
                rect = QRect(j*sizex, i*sizey, sizex, sizey) #координаты края клетки               
                
                if self.field.list_field[i][j].color == QColor.green:
                    p.fillRect(rect, QColor(0,255,0))
                if self.field.list_field[i][j].color == QColor.yellow:
                    p.fillRect(rect, QColor(255,255,0))
                if self.field.list_field[i][j].color == QColor.red:
                    p.fillRect(rect, QColor(255,0,0))
                if self.field.list_field[i][j].color == QColor.blue:
                    p.fillRect(rect, QColor(0,0,255))
                if self.field.list_field[i][j].choisen:
                    p.fillRect(rect, QColor(0,255,255))
                p.drawRect(rect)
                
             
    def mousePressEvent(self, e):
        if (self.frame.x() < e.x() < self.frame.x()+self.frame.width()) & (self.frame.y() < e.y() < self.frame.y()+self.frame.height()):   
            i = int((e.x() - self.frame.x())//(self.frame.width()/len(self.field.list_field[0])))
            j = int((e.y() - self.frame.y())//(self.frame.height()/len(self.field.list_field)))   
            
            self.tmp_array = [j, i]
            ##############
            if not self.field.list_field[j][i].choisen:
                self.field.ChoisenUnit(j, i)   
                self.numcho=1
            ##############
        self.update()
    
    def mouseMoveEvent(self, e):
        if (self.frame.x() < e.x() < self.frame.x()+self.frame.width()) & (self.frame.y() < e.y() < self.frame.y()+self.frame.height()):   
            i = int((e.x() - self.frame.x())//(self.frame.width()/len(self.field.list_field[0])))
            j = int((e.y() - self.frame.y())//(self.frame.height()/len(self.field.list_field))) 
            
            for neig in CastleGame.Field.GetNeighbourhood(self.tmp_array[0], self.tmp_array[1], self.field.list_field):
                ###################
                if self.field.list_field[j][i] == neig:
                    ###############
                    if self.field.list_field[j][i].color == self.field.list_field[self.tmp_array[0]][self.tmp_array[1]].color and not self.field.list_field[j][i].choisen:
                        self.field.ChoisenUnit(j, i) 
            ######################
                        self.numcho+=1
                        self.tmp_array = [j, i]
                        break
            #####################
            self.update()
        
    def mouseReleaseEvent(self, e):
        if self.numcho > 2:
            self.field.DeleteShape()
            self.field.EndGame()
        else:
            for line in self.field.list_field:
                for el in line:
                    el.choisen = False
        self.labelScore.setText(str(self.field.score))
        self.update()     
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = mainForm()
    form.show()
    app.exec()
    
        

