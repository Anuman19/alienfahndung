from turtle import *
from functions import *
eckig = False
run = True
rund = False



while run == True:
    kopfform = input("Ist der Kopf rund oder eckig? ")
    kopfform = kopfform.lower()
    if kopfform == "rund":                                 #Wenn Antwort rund --> beende Schleife, setze rund == True
        print("Okay rund also")
        run = False
        rund = True
    elif kopfform == "eckig":
        print("Okay eckig also")                           #Wenn Antwort eckig --> beende Schleife, setze eckig == True
        run = False
        eckig = True
    else:
        print("Als rund bezeichnet man die Form eines Kreises, im Wesentlichen ohne Ecken und Kanten!")     #Definitionen von rund und eckig von Duden
        print("Unter eckig versteht man Formen welche Ecken aufweisen!")

zahlene = False
zahlengrösse = False
zahlenr = False


if rund == True:
    print("Unsere HD Kameras haben den Radius des besagten Kopfes zwischen 5-150 festgelegt...")
    radius = input("Wie gross ist denn der Radius des Alienkopfes? ")
    zahlenr = checkradius(radius)

    while not zahlenr:
        radius = input("Bitte gib eine Zahl zwischen 5-150 ein! ")
        zahlenr = checkradius(radius)
if zahlenr:
        drawcircle_kopf(radius)



if eckig:
    ecken = input("Das Alien hat nach ihren Angaben einen Kopf mit Ecken...\nNach unseren Angaben ist die Anzahl Ecken zwischen 3-10.\nWie viele Ecken haben Sie gesehen? ")
    zahlene = checkeck(ecken)
    while not zahlene:
        ecken = input("Bitte gib eine natürliche Zahl zwischen 3 und 10 ein! ")
        zahlene = checkeck(ecken)

if zahlene:
    grösse = input("Mal angenommen das Alien hat wirklich " + ecken +" Ecken...zwischen 1-100, wie gross würden Sie eine Seite einschätzen? ")
    zahlengrösse = checkgröss(grösse)
    while not zahlengrösse:
        print("Bitte gib eine natürliche Zahl zwischen 1 und 100 ein!")
        grösse = input("Wie gross ist die Seite? ")
        zahlengrösse = checkgröss(grösse)
    drawpolygon_kopf(ecken, grösse)













