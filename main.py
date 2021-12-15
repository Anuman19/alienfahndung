from turtle import *
from polyHead import *
from roundHead import *
from functions import *

print("WELCOME TO AREA 51.3! \n"
      "As you are well aware there were several sightings of unknown entities. \n"
      "Our department has received the information that you might have some insight into this matter \n"
      "The source of this information is almost trustworthy which is why you were brought here with a bag over your head \n"
      "and what some might describe as violently. \n"
      "But fear not dear citizen. You are only here to provide a description of the creature in question. \n"
      "Your country will be grateful for your contribution! \n"
      "Now, let us start from the top.")
error = 0

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
    if Poly.cheeseCheck(cheese):
        break
    else:
        print("Please choose a value between 1 - 10.")
        continue

if headForm:
    print("Hmmmm....round you say. \n"
          "That is indeed interesting because our scouting team also described its head as round... \n"
          "They reported the radius to be anywhere between 5 and 100.")
    head = Round()
    while True:
        try:
            headRadius = int(input("What would you say is the radius of this head? "))
        except ValueError:
            print("This is not a valid answer citizen!")
            error += 1
            continue
        if head.radiusCheck(headRadius):
            break
        else:
            print("Our scouts are professionals. They are sure the value is between 5 - 100.")
            continue
else:
    print("Hmmmm....angular you say. \n"
          "That is indeed interesting because our scouting team also described its head as angular... \n"
          "They reported the number of corners to be anywhere between 4 and 8.")
    head = Poly()
    run = True
    while run:
        try:
            corner = int(input("How many corners are there? "))
        except ValueError:
            print("This is not a valid answer citizen!")
            error += 1
            continue
        if head.cornerCheck(corner):
            print("Hmmm...I believe you this time. \n"
                  "One of our scouts managed to get rather close to the creature. \n"
                  "Because of that he was able to measure one side of its head! \n"
                  "But he was eaten in the process. :( \n"
                  "The brave soldiers last screams were that the length is anywhere between 10 - 100. ")
            while True:
                try:
                    line = int(input("What would you say is the length? "))
                except ValueError:
                    print("This is not a valid answer citizen!")
                    error += 1
                    continue
                if head.lineCheck(line):
                    run = False
                    break
                else:
                    print("Are you insulting the sacrifice of my brave scout??")
                    continue
        else:
            print("Our scouts are professionals. They are sure the value is between 4 - 10.")
            continue

while True:
    bodyForm = input("Would you describe the body of the creature as (r)ound or (a)ngular? ")
    if bodyForm.lower() == "r" or bodyForm.lower() == "round":
        bodyForm = True
        break
    elif bodyForm.lower() == "a" or bodyForm.lower() == "angular":
        bodyForm = False
        break
    else:
        print("Press r for round or a for angular.")
        continue

if bodyForm:
    body = head
    while True:
        try:
            bodyRadius = int(input("What would you say is the radius of this body? "))
        except ValueError:
            print("This is not a valid answer citizen!")
            error += 1
            continue
        if body.radiusCheck(bodyRadius):
            break
        else:
            print("Our scouts are professionals. They are sure the value is between 5 - 100.")
            continue
else:
    body = head
    run = True
    while run:
        try:
            bodyCorner = int(input("How many corners are there? "))
        except ValueError:
            print("This is not a valid answer citizen!")
            error += 1
            continue
        if head.cornerCheck(bodyCorner):
            print("Hmmm...I believe you this time. \n")
            while True:
                try:
                    bodyLine = int(input("What would you say is the length? "))
                except ValueError:
                    print("This is not a valid answer citizen!")
                    error += 1
                    continue
                if head.lineCheck(bodyLine):
                    run = False
                    break
                else:
                    print("Are you insulting the sacrifice of my brave scout??")
                    continue
        else:
            print("Our scouts are professionals. They are sure the value is between 4 - 10.")
            continue

while True:
    bodyForm = input("Would you describe the body of the creature as (r)ound or (a)ngular? ")
    if bodyForm.lower() == "r" or bodyForm.lower() == "round":
        bodyForm = True
        break
    elif bodyForm.lower() == "a" or bodyForm.lower() == "angular":
        bodyForm = False
        break
    else:
        print("Press r for round or a for angular.")
        continue

if bodyForm:
    body = head
    while True:
        try:
            bodyRadius = int(input("What would you say is the radius of this body? "))
        except ValueError:
            print("This is not a valid answer citizen!")
            error += 1
            continue
        if body.radiusCheck(bodyRadius):
            break
        else:
            print("Our scouts are professionals. They are sure the value is between 5 - 100.")
            continue
else:
    body = head
    bodyRun = True
    while bodyRun:
        try:
            bodyCorner = int(input("How many corners are there?"))
        except ValueError:
            print("This is not a valid answer citizen!")
            error += 1
            continue
        if body.cornerCheck(bodyCorner):
            print("Hmmm...I believe you this time.")
            while True:
                try:
                    bodyLine = int(input("What would you say is the length? "))
                except ValueError:
                    print("This is not a valid answer citizen!")
                    error += 1
                    continue
                if body.lineCheck(bodyLine):
                    bodyRun = False
                    break
                else:
                    print("Are you insulting the sacrifice of my brave scout??")
                    continue
        else:
            print("Our scouts are professionals. They are sure the value is between 4 - 10.")
            continue

if headForm:
    drawborder()
    head = Round()
    head.drawroundhead(headRadius, cheese)
else:
    drawborder()
    head = Poly()
    head.drawpolyhead(corner, line, cheese)

if bodyForm:
    drawborder()
    body = Round()
    body.setSection(0)
    body.drawroundhead(bodyRadius, cheese)
else:
    drawborder()
    body = Poly()
    body.setSection(0)
    body.drawpolyhead(bodyCorner, bodyLine, cheese)

done()
