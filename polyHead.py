from turtle import *
import math

from alienfahndung.functions import colors


class Poly:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.ht()
        self.turtle.speed(10)
        self.turtle.up()
        self.turtle.goto(0, 200)
        self.turtle.down()

    section = 100

    def drawpolyhead(self, corner, line, colour):
        self.turtle.up()
        self.turtle.goto(0 - line / 2, self.section)
        self.turtle.down()
        self.turtle.color("black", colors[int(colour)])
        self.turtle.begin_fill()

        for i in range(corner):
            self.turtle.fd(line)
            self.turtle.lt(360 / corner)
        self.turtle.end_fill()
        self.turtle.ht()

    def setSection(self, value):
        self.section = value
