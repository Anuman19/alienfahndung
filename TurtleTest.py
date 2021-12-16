from polyHead import *
from functions import *


def radius(corner, line):
    return line / (2 * math.sin(math.degrees(180 / corner)))


# corner = 10
# side = 100
# print(radius(corner, side))
# print(radius(corner,side) * (2 * math.sin(math.degrees(180 / corner))))
#
# turtle = Turtle()
#
# turtle.pensize(30)
# turtle.goto(0,10)
# turtle.fd(100)
# done()

import math

turtle = Turtle()
turtle.color('blue')

turtle.speed(50)

for i in range(45):
    turtle.forward(150)
    turtle.left(170)
turtle.ht()
done()
