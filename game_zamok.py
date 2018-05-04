# -*- coding: utf-8 -*-

class Figure():
    def __init__(self, x, y, color, choise):
        self.x = x
        self.y = y
        self.choise = choise
        self.color = color
import random 
       
class Field():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.list_field = []
        
        for i in range(height):
            tmp = []
            for j in range(width):
                  tmp.append(random.randint(0,4))
            self.list_field.append(tmp)
def out_matrix():
    
    