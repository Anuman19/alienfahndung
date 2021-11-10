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

    def radiusCheck(self, radius):

        if radius > 1:
            return not (radius < 5 or radius > 100)
        else:
            return False

    def drawroundhead(self, radius, cheese):

        self.turtle.up()
        self.turtle.goto(0, 100)
        self.turtle.down()
        self.turtle.down()
        self.turtle.color("black", colors[int(cheese) - 1])
        self.turtle.begin_fill()
        self.turtle.circle(radius)
        self.turtle.end_fill()
