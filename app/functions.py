from turtle import *


def draw_border():
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
def line_check(corner, line):
    if 4 < corner < 7 and line > 80:
        line = 80
    elif 6 < corner <= 10 and line > 70:
        line = 60
    return line


def set_body_radius(size):
    switch = {
        1: 30,
        2: 60,
        3: 90
    }
    return switch.get(size, "Invalid")


def draw_extension(x, y, direction, colour):
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


def star():
    turtle = Turtle()
    turtle.color('blue')
    turtle.speed(50)
    turtle.penup()
    turtle.goto(-250, -200)
    turtle.pendown()
    turtle.color("orange")
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(150)
        turtle.left(144)

    turtle.end_fill()
    turtle.ht()


def write_name(name):
    turtle = Turtle()
    turtle.ht()
    turtle.penup()
    turtle.goto(0, 310)
    turtle.pendown()
    turtle.write(name, False, align="center", font=("Arial", 50, "italic"))
