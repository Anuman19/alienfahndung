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

zahlen = False
zahlengrösse = False

"""
while rund == True:
    radius = input("Wie gross ist denn der Alienkopf in Zahlen? ")
    zahlen = radius.isdigit()
    if zahlen == True:
        rund = False
        radius = int(radius)
        drawcircle_kopf(radius)
    else:
        print("Bitte gib eine Zahl ein!")
        rund = True """

if eckig:
    ecken = input("Das Alien hat nach ihren Angaben einen Kopf mit Ecken...\nNach unseren Angaben ist die Anzahl Ecken zwischen 3-10.\nWie viele Ecken haben Sie gesehen? ")
    zahlen = checkeck(ecken)
    while not zahlen:
        ecken = input("Bitte gib eine natürliche Zahl zwischen 3 und 10 ein! ")
        zahlen = checkeck(ecken)

if zahlen:
    grösse = input("Mal angenommen das Alein hat wirklich " + ecken +" Ecken...zwischen 1-100, wie gross würden Sie eine Seite einschätzen? ")
    zahlengrösse = checkgröss(grösse)
    while not zahlengrösse:
        print("Bitte gib eine natürliche Zahl zwischen 1 und 100 ein!")
        grösse = input("Wie gross ist die Seite? ")
        zahlengrösse = checkgröss(grösse)
    drawpolygon_kopf(ecken, grösse)













