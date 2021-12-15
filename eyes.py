from turtle import *
import math
from polyHead import *


class Eyes():

    def __init__(self, offset):
        self.turtle = Turtle()
        self.turtle.ht()
        self.turtle.speed(10)
        self.turtle.up()
        self.turtle.seth(0)
        self.turtle.goto(0 - offset/2, 200 - offset)
        self.turtle.down()

    def drawEyes(self, size):

        if size >= 50:
            for i in range(2):
                self.turtle.seth(-45)
                self.turtle.color("black")
                self.turtle.begin_fill()
                self.turtle.circle(10, 90)
                self.turtle.circle(5, 90)
                self.turtle.circle(10, 90)
                self.turtle.circle(5, 90)
                self.turtle.end_fill()
                self.turtle.up()
                self.turtle.seth(0)
                self.turtle.fd(50)
                self.turtle.down()
