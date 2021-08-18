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

def drawpolygon_kopf(ecken, grösse):
    ecken = abs(ecken)
    grösse = abs(grösse)
    t_kopf = Turtle()
    t_kopf.up()
    t_kopf.goto(0-grösse/2, 300)
    t_kopf.down()
    for i in range(ecken):
        t_kopf.fd(grösse)
        t_kopf.right(360/ecken)

def checkeck(ecken):
    zahl = ecken.isdigit()
    if not zahl:
        return False
    elif zahl:
        ecken = float(ecken)
        if ecken > 10 or ecken < 3:
            return False
        else:
            return True




def checkgröss(grösse):
    zahl = grösse.isdigit()
    if not zahl:
        return False
    elif zahl:
        grösse = float(grösse)
        grösse = abs(grösse)
        if grösse > 100:
            return False
    else:
        return True



    done()

def drawcircle_kopf(radius):
    t_kopf = Turtle()
    t_kopf.circle(radius)
    done()



