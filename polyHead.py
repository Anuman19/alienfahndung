from turtle import *
import math

colors = [

    "crimson",
    "deeppink",
    "orange",
    "lime",
    "green",
    "cyan",
    "navy",
    "gold",
    "yellow",
    "magenta"

]


class Poly:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.ht()
        self.turtle.speed(10)
        self.turtle.up()
        self.turtle.goto(0, 200)
        self.turtle.down()

    section = 200

    @staticmethod
    def cornerCheck(corner):

        if corner > 1:

            return not (corner < 4 or corner > 8)
        else:
            return False

    @staticmethod
    def lineCheck(line):

        if line > 1:
            return not (line < 10 or line > 100)
        else:
            return False

    @staticmethod
    def cheeseCheck(cheese):

        if cheese > 1:
            return not (cheese < 1 or cheese > 10)
        else:
            return False

    def drawpolyhead(self, corner, line, cheese):

        line = self.radius(corner, line)
        self.turtle.up()
        self.turtle.goto(0 - line / 2, self.section)
        self.turtle.down()
        self.turtle.color("black", colors[int(cheese) - 1])
        self.turtle.begin_fill()

        for i in range(corner):
            self.turtle.fd(line)
            self.turtle.lt(360 / corner)
        self.turtle.end_fill()
        self.turtle.ht()
        done()

    @staticmethod
    def checkApothem(corner, line):

        radius = Poly.radius(corner, line)

        if radius >= 90:
            while radius >= 90:
                radius -= 1
            print(radius)
            return Poly.radius(corner, line) * (2 * math.sin(math.degrees(180 / corner)))

        else:
            return line

    @staticmethod
    def radius(corner, line):
        return line / (2 * math.sin(math.degrees(180 / corner)))

    def setSection(self, value):
        self.section = value
