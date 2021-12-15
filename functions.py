from turtle import *


def drawborder():
    border = Turtle()
    border.ht()
    border.speed(10)
    border.up()
    border.goto(-300, -300)
    border.down()
    for i in range(4):
        border.fd(600)
        border.lt(90)


colors = {

    1: "crimson",
    2: "deeppink",
    3: "orange",
    4: "lime",
    5: "green",
    6: "cyan",
    7: "navy",
    8: "gold",
    9: "yellow",
    10: "magenta"

}


def cheeseCheck(cheese):
    return 1 <= cheese <= 10


def radiusCheck(radius):
    return 25 <= radius <= 100


def cornerCheck(corner):
    return 4 <= corner <= 10


def lineCheck(corner, line):
    if 4 < corner < 7 and line > 80:
        line = 80
    elif 6 < corner <= 10 and line > 70:
        line = 60
    return line


def setBodyRadius(size):
    switch = {
        1: 30,
        2: 60,
        3: 90
    }
    return switch.get(size, "Invalid")


def drawExtension(x, y, direction):
    turtle = Turtle()
    turtle.ht()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.pensize(15)
    if direction == 0:
        turtle.seth(260)
    elif direction == 1:
        turtle.seth(280)
    elif direction == 2:
        turtle.seth(190)
    elif direction == 3:
        turtle.seth(-10)
    turtle.fd(100)


def draw():
    turtle = Turtle()
    turtle.ondrag(turtle.goto)
