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

        line = self.apothem(corner, line)
        self.turtle.up()
        self.turtle.goto(0 - line / 2, 100)
        self.turtle.down()
        self.turtle.color("black", colors[int(cheese) - 1])
        self.turtle.begin_fill()

        for i in range(corner):
            self.turtle.fd(line)
            self.turtle.lt(360 / corner)
        self.turtle.end_fill()
        self.turtle.ht()

    @staticmethod
    def checkApothem(corner, line):

        a = line / (2 * math.sin(math.pi / corner))

        if a >= 90:
            while a >= 90:
                a -= 1
            print(a)
            return round((a * 2 * math.tan(math.pi / corner)) / 10) * 10

        else:
            return line

    @staticmethod
    def apothem(corner, line):
        return line / (2 * math.tan(math.pi / corner))
