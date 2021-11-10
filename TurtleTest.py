from turtle import *
from functions import *
from polyHead import PolyHead
from roundHead import RoundHead

turtrand = Turtle()
drawborder(turtrand)

turtle = Turtle()

turtle.speed(10)
turtle.color("violet")
turtle.ht()
turtle.up()
turtle.goto(-300, 100)
turtle.down()
turtle.fd(600)
turtle.up()
turtle.goto(-300, -100)
turtle.down()
turtle.fd(600)
head = RoundHead()
print(head.checkRadius("100"))


done()
