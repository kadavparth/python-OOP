#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 12:58:39 2022

@author: parth
"""
from random import randint
import turtle

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rect(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.x < self.y < rectangle.point2.y:
            print("your guess lies within the rectangle")
        else:
            print("your guess lise outside the rectangle")

class GuiPoint(Point):

    def draw(self,canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size,color)

class Rectangle:
    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        print((self.point2.x - self.point1.x) * (self.point2.y - self.point1.y), "unit^2")


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x,self.point1.y)
        canvas.pendown()

        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

rectangle = GuiRectangle(
    Point(randint(0,400),randint(0,400)),
    Point(randint(10,400),randint(10,400))
    )

print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

user_point = GuiPoint(float(input("Guess x:")),float(input("Guess y:")))
rectangle.area()
user_point.falls_in_rect(rectangle)

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)

turtle.done()