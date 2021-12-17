import turtle
from turtle import *


class Leg:

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.ht()
        self.turtle.speed(10)
        self.turtle.up()
        self.turtle.seth(0)
        self.turtle.goto(0, 0)
        self.turtle.down()


