import numpy as np
from PIL import Image

class Canvas:
    def __init__(self,width,height,color):
        self.width = width
        self.height =height
        self.color =color

        if self.color == 'black':
            self.color = [0,0,0]
        elif self.color == 'white':
            self.color = [255,255,255]
        else:
            pass
        self.emparr = np.zeros((self.width,self.height,3), dtype=np.uint8)
        self.emparr[:] = self.color

    def make(self):
        img = Image.fromarray(self.emparr, 'RGB')
        img.save('canvas.png')

class Rectangle:

    def __init__(self,pt1,pt2,color):
        self.pt1 = pt1
        self.pt2 = pt2
        self.color = color
        self.x1,self.y1 = self.pt1
        self.x2,self.y2 = self.pt2
        if self.color == 'red':
            self.color = [255,0,0]
        else:
            pass

    def draw(self,canvas):
        canvas.emparr[self.x1:self.x2,self.y1:self.y2] = [self.color]
        canvas.make()

class Square:

    def __init__(self,pt1,size,color):
        self.pt1 = pt1
        self.x1, self.y1 = self.pt1
        self.size = size
        self.color = color

        if self.color == 'red':
            self.color = [255, 0, 0]
        elif self.color == 'black':
            self.color = [0,0,0]
        else:
            self.color = [255,255,0]

    def draw(self,canvas):
        canvas.emparr[self.x1:(self.x1+self.size), self.y1:(self.y1+self.size)] = [self.color]
        canvas.make()

canvas1 = Canvas(700,700,'white')
canvas1.make()

rectangle = Rectangle((150,150),(400,300),'red')
rectangle.draw(canvas1)

rectangle1 = Rectangle((600,600),(700,700),'red')
rectangle1.draw(canvas1)

square = Square((250,250),100,'black')
square.draw(canvas1)

