from turtle import *

def kopfpolygon(ecken):
    t_kopf = Turtle()
    t_kopf.up()
    t_kopf-goto(350, 400)
    t_kopf.down()
    t_kopf.ht()
    for i in range(ecken):
        t_kopf.fd(50)
        t_kopf.right(360/ecken)
    done()

def kopfkreis(radius):
    t_kopf = Turtle()
    t_kopf.circle(radius)
    done()