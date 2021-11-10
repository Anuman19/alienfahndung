from turtle import *
from functions import *
from eyes import *
from roundHead import *



drawborder()

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
head = Poly()
head.drawpolyhead(10, 200, 5)
# print(head.radiusCheck("100"))
print(head.checkApothem(4,200))
print(100 / (2 * math.sin(math.pi / 4)))

# eyes = Eyes(head.apothem(5,100))
# eyes.drawEyes(50)


done()
