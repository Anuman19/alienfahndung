from turtle import *
import math
from polyHead import *


class Round:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.ht()
        self.turtle.speed(10)
        self.turtle.up()
        self.turtle.goto(0, 0)
        self.turtle.down()

    section = 100

    def drawroundhead(self, radius, colour):
        self.turtle.up()
        self.turtle.goto(0, self.section)
        self.turtle.down()
        self.turtle.color("black", colors[int(colour)])
        self.turtle.begin_fill()
        self.turtle.circle(radius)
        self.turtle.end_fill()

    def setSection(self, value):
        self.section = value
