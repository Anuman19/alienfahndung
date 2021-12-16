from roundHead import *
from functions import *
from eyes import *

print("WELCOME TO AREA 50.0! \n"
      "As you are well aware there were several sightings of unknown entities. \n"
      "Our department has received the information that you might have some insight into this matter \n"
      "The source of this information is almost trustworthy, \n"
      "which is why you were brought here with a bag over your head\n"
      "and what some might describe as violently. \n"
      "But fear not dear citizen. You are only here to provide a description of the creature in question. \n"
      "Your country will be grateful for your contribution! \n"
      "Now, let us start from the top. \n")

error = 0
headRadius = 0
cheese = 0
magikarp = 0
corner = 0
headPolySide = 0
bodyRadius = 0
legs = 0
arms = 0

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
    if 1 <= cheese <= 10:
        break
    else:
        print("Please choose a value between 1 - 10.")
        error += 1
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
        if 25 <= headRadius <= 100:
            break
        else:
            print("Our scouts are professionals. They are sure the value is between 25 - 100.")
            error += 1
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
        if 4 <= corner <= 10:
            print("Hmmm...I believe you this time. \n"
                  "One of our scouts managed to get rather close to the creature. \n"
                  "Because of that he was able to get a closer look of its head! \n"
                  "But he was eaten in the process. :( \n"
                  "The brave soldiers last screams were that he loved serving his country.... \n")
            break
        else:
            print("Our scouts are professionals. They are sure the value is between 4 - 10.")
            error += 1
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
            error += 1
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

while True:
    try:
        magikarp = int(input("On scale 1 - 10 where 1 is not likely and 10 is very likely, \n"
                             "how likely is it that you would sacrifice your life for a Magikarp? "))
    except ValueError:
        print("This is not a valid answer citizen!")
        error += 1
        continue
    if 1 <= magikarp <= 10:
        if magikarp <= 5:
            print("My disappointment is immeasurable and my day ruined.")
        else:
            print("Splash")
        break
    else:
        print("Magikarp is a Fish.")
        error += 1
        continue

print("Now lets get back to the important stuff!\n")
print(colors)

while True:
    try:
        legs = int(input("Please choose the most fitting colour for the legs: "))
    except ValueError:
        print("This is not a valid answer citizen!")
        error += 1
        continue
    if 1 <= legs <= 10:
        print("Interesting...")
        break
    else:
        print("Press a number between 1 - 10.")
        error += 1
        continue

print(colors)
while True:
    try:
        arms = int(input("Please choose the most fitting colour for the arms: "))
    except ValueError:
        print("This is not a valid answer citizen!")
        error += 1
        continue
    if 1 <= arms <= 10:
        print("Very interesting...")
        break
    else:
        print("Press a number between 1 - 10.")
        error += 1
        continue

if error == 0:
    print("My dear Sir. You have answered every question of mine correctly and honestly.\n"
          "This is why my consciousness forces me to tell you the truth...\n"
          "There is no Area 50.0.\n"
          "There are no aliens.\n"
          "This is a military hospital in Atlanta.\n"
          "You tripped on your way to your job as Commander of the distracting unit.\n"
          "What you are about to see is a portrait of what you look like now.\n"
          "We tried our best to restore your former glory....\n"
          ".............\n"
          "and we are glad to say we surpassed every expectation!")
else:
    print("Dear Citizen. You answered me incorrectly ", error, " times.\n" +
          "This is unacceptable!!\n"
          "But I guess it was no use to expect more of you.\n"
          "................\n"
          "Based on your description of the alien in question,\n"
          "you seem to have successfully seen through my scheme.\n"
          "Yes, this is Area 50.0.\n"
          "And yes...\n"
          "You are the alien we have captured\n"
          "and yes you will be dissected!\n")

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
# body
roundObj.setSection(angular.section - 2 * bodyRadius)
roundObj.drawroundhead(bodyRadius, magikarp)

# legs
drawExtension(-10, angular.section - 2 * bodyRadius, 260, legs)
drawExtension(10, angular.section - 2 * bodyRadius, 280, legs)

# arms
drawExtension(0 - bodyRadius, 100 - bodyRadius, 190, arms)
drawExtension(0 + bodyRadius, 100 - bodyRadius, -10, arms)

done()
