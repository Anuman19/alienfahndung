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


def drawExtension(x, y, direction, colour):
    turtle = Turtle()
    turtle.ht()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.pensize(12)
    turtle.seth(direction)
    turtle.pencolor(colors[colour])
    turtle.begin_fill()
    turtle.fd(100)
    turtle.end_fill()


def draw():
    turtle = Turtle()
    turtle.ondrag(turtle.goto)
