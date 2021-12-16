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


# resize HeadSide to fit the borders.
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


def sign():
    turtle = Turtle()
    turtle.speed(15)
    turtle.penup()
    turtle.goto(-30, -280)
    turtle.pendown()
    turtle.ondrag(turtle.goto)


# https://techpluslifestyle.com/technology/turtle-library-python/
def heart():
    turtle = Turtle()
    turtle.ht()
    turtle.speed(50)
    turtle.penup()
    turtle.goto(200, -300)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor('red')
    turtle.left(140)
    turtle.forward(90)
    turtle.circle(-45, 200)
    turtle.setheading(60)
    turtle.circle(-45, 200)
    turtle.forward(90)
    turtle.end_fill()


# https://techpluslifestyle.com/technology/turtle-library-python/
def star():
    turtle = Turtle()
    turtle.color('blue')
    turtle.speed(50)
    turtle.penup()
    turtle.goto(-250, -200)
    turtle.pendown()
    for i in range(45):
        turtle.forward(150)
        turtle.left(170)
    turtle.ht()
