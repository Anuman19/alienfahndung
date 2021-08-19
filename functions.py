from turtle import *


def drawborder(turtrand):
    turtrand.ht()
    turtrand.speed(10)
    turtrand.up()
    turtrand.goto(-350,-350)
    turtrand.down()
    for i in range(4):
        turtrand.fd(700)
        turtrand.lt(90)

def drawpolygon_kopf(ecken, grösse, color):
    turtrand = Turtle()
    drawborder(turtrand)
    ecken = int(ecken)
    grösse = int(grösse)
    ecken = abs(ecken)
    grösse = abs(grösse)
    t_kopf = Turtle()
    t_kopf.up()
    t_kopf.goto(0-grösse/2, 300)
    t_kopf.down()
    t_kopf.color("black", color)
    t_kopf.begin_fill()
    for i in range(ecken):
        t_kopf.fd(grösse)
        t_kopf.right(360/ecken)
    t_kopf.end_fill()
    t_kopf.ht()
    done()

def checkeck(ecken):
    zahl = ecken.isdigit()
    if not zahl:
        return False
    elif zahl:
        ecken = int(ecken)
        if ecken > 10 or ecken < 3:
            return False
        else:
            return True




def checkgröss(grösse):
    zahl = grösse.isdigit()
    if not zahl:
        return False
    elif zahl:
        grösse = int(grösse)

        if grösse > 100:
            return False
        elif grösse < 1:
            return False
        else:
            return True

def drawcircle_kopf(radius, color):
    turtrand = Turtle()
    drawborder(turtrand)
    radius = int(radius)
    t_kopf = Turtle()
    t_kopf.up()
    t_kopf.goto(0, 300-2*radius)
    t_kopf.down()
    t_kopf.color("black", color)
    t_kopf.begin_fill()
    t_kopf.circle(radius)
    t_kopf.end_fill()
    t_kopf.ht()

    done()

def checkradius(radius):
    zahl = radius.isdigit()
    if not zahl:
        return zahl
    else:
        radius = int(radius)
        if radius < 5:
            return False
        elif radius > 150:
            return False
        else:
            return True

kopf_colors = {

    1 : "crimson",
    2 : "deeppink",
    3 : "orange",
    4 : "lime",
    5 : "green",
    6 : "cyan",
    7 : "navy",
    8 : "gold",
    9 : "yellow",
    10 : "magenta"

}



