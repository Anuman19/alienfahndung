import math

from polyHead import *
from functions import *


def radius(corner, line):
    return line / (2 * math.sin(math.degrees(180 / corner)))


# turtle = Turtle()
# turtle.color('blue')
# turtle.speed(50)
# turtle.penup()
# turtle.goto(-250, -200)
# turtle.pendown()
# turtle.color("orange")
# turtle.begin_fill()
# for i in range(5):
#     turtle.forward(150)
#     turtle.left(144)
#
# turtle.end_fill()
# turtle.ht()

done()
