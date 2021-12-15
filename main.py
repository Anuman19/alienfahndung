from turtle import *

from alienfahndung.extensions import Leg
from polyHead import *
from roundHead import *
from functions import *
from eyes import *

print("WELCOME TO AREA 51.3! \n"
      "As you are well aware there were several sightings of unknown entities. \n"
      "Our department has received the information that you might have some insight into this matter \n"
      "The source of this information is almost trustworthy which is why you were brought here with a bag over your head \n"
      "and what some might describe as violently. \n"
      "But fear not dear citizen. You are only here to provide a description of the creature in question. \n"
      "Your country will be grateful for your contribution! \n"
      "Now, let us start from the top. \n")

error = 0
headRadius = 0
cheese = -1
corner = 0
headPolySide = 0
bodyRadius = 0

while True:
    headForm = input("Would you describe the head of the creature as (r)ound or (a)ngular? ")
    if headForm.lower() == "r" or headForm.lower() == "round":
        headForm = True
        break
    elif headForm.lower() == "a" or headForm.lower() == "angular":
        headForm = False
        break
    else:
        print("Press r for round or a for angular.")
        continue
print("By the way, i really love cheese. \n"
      "Unfortunately there are some lost souls who in fact do not engulf cheese in affection \n")
while True:
    try:
        cheese = int(input("How would you rate your liking to cheese on a scale 1 - 10? "))
    except ValueError:
        print("This is not a valid answer cheetizen!")
        error += 1
        continue
    if cheeseCheck(cheese):
        break
    else:
        print("Please choose a value between 1 - 10.")
        continue

if headForm:
    print("Hmmmm....round you say. \n"
          "That is indeed interesting because our scouting team also described its head as round... \n"
          "They reported the radius to be anywhere between 25 and 100.")
    while True:
        try:
            headRadius = int(input("What would you say is the radius of this head? "))
        except ValueError:
            print("This is not a valid answer citizen!")
            error += 1
            continue
        if radiusCheck(headRadius):
            break
        else:
            print("Our scouts are professionals. They are sure the value is between 25 - 100.")
            continue
else:
    print("Hmmmm....angular you say. \n"
          "That is indeed interesting because our scouting team also described its head as angular... \n"
          "They reported the number of corners to be anywhere between 4 and 10. \n")

    while True:
        try:
            corner = int(input("How many corners are there? "))
        except ValueError:
            print("This is not a valid answer citizen!")
            error += 1
            continue
        if cornerCheck(corner):
            print("Hmmm...I believe you this time. \n"
                  "One of our scouts managed to get rather close to the creature. \n"
                  "Because of that he was able to get a closer look of its head! \n"
                  "But he was eaten in the process. :( \n"
                  "The brave soldiers last screams were that he loved serving his country.... \n")
            break
        else:
            print("Our scouts are professionals. They are sure the value is between 4 - 10.")
            continue

    while True:
        try:
            headPolySide = int(input("What would you say is the length? (50 - 100) "))
        except ValueError:
            print("This is not a valid answer citizen!")
            error += 1
            continue
        if 50 <= headPolySide <= 100:
            headPolySide = lineCheck(corner, headPolySide)
            break
        else:
            print("Are you insulting the sacrifice of my brave scout??")
            continue

if headForm:
    print("So far you have...")
else:
    print("...")

print("Now let us talk about the body. \n")
print("Please choose the word which you think is the most accurate in regards to its size: ")

while True:
    try:
        bodyRadius = int(input(" marble(1) | basketball(2) | planet(3) "))
    except ValueError:
        print("This is not a valid answer citizen!")
        error += 1
        continue
    if bodyRadius == 1 or bodyRadius == 2 or bodyRadius == 3:
        bodyRadius = setBodyRadius(bodyRadius)
        break
    else:
        print(" marble(1) | basketball(2) | planet(3) ")
        print("Please choose one of the internationally accepted sizes for aliens by pressing 1,2 or 3.")
        continue

roundObj = Round()
angular = Poly()

if headForm:
    drawborder()
    roundObj.drawroundhead(headRadius, cheese)
    eyes = Eyes(0 - headRadius / 2, roundObj.section + headRadius)
    if headRadius < 50:
        eyes.drawEye()
    else:
        eyes.drawEyes()
else:
    drawborder()
    angular.drawpolyhead(corner, headPolySide, cheese)
    if headPolySide <= 65 or corner <= 5:
        eyes = Eyes(0 / 2, 100 + 20)
        eyes.drawEye()
    else:
        eyes = Eyes(0 - 50 / 2, 100 + 20)
        eyes.drawEyes()

roundObj.setSection(angular.section - 2 * bodyRadius)
roundObj.drawroundhead(bodyRadius, cheese)
drawExtension(0, angular.section - 2 * bodyRadius, 0)
drawExtension(0, angular.section - 2 * bodyRadius, 1)

drawExtension(0 - bodyRadius, 100 - bodyRadius, 2)
drawExtension(0 + bodyRadius, 100 - bodyRadius, 3)

done()
