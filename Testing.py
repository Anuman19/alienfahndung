from turtle import *
from functions import *


poly = False
running = True
circle = False



while running:
    headform = input("Ist der Kopf rund oder eckig? ")
    headform = headform.lower()
    if headform == "rund":                                 #Wenn Antwort rund --> beende Schleife, setze rund == True
        print("Okay rund also")
        running = False
        circle = True
    elif headform == "eckig":
        print("Okay eckig also")                           #Wenn Antwort eckig --> beende Schleife, setze eckig == True
        running = False
        poly = True
    else:
        print("Als rund bezeichnet man die Form eines Kreises, im Wesentlichen ohne Ecken und Kanten!")     #Definitionen von rund und eckig von Duden
        print("Unter eckig versteht man Formen welche Ecken aufweisen!")

digitradius = False

digitcount = False

digitround = False


if circle:
    print("Unsere HD Kameras haben den Radius des besagten Kopfes zwischen 5-150 festgelegt...")
    radius = input("Wie gross ist denn der Radius des Alienkopfes? ")
    digitradius = checkradius(radius)

    while not digitradius:
        radius = input("Bitte gib eine Zahl zwischen 5-150 ein! ")
        digitradius = checkradius(radius)
    cheese = input("Nebenbei, auf einer Skala von 1 bis 10, wie sehr magst du Käse? ")
    cheese = checkoneten(cheese)
    while not cheese:
        print("Bitte Gib eine Zahl zwischen 1-10 ein!")
        cheese = input("Wie sehr magst du Käse? ")
        cheese = checkoneten(cheese)
    drawcircle_kopf(radius, cheese)





if poly:
    polyin = input("Das Alien hat nach ihren Angaben einen Kopf mit Ecken...\nNach unseren Angaben ist die Anzahl Ecken zwischen 3-10.\nWie viele Ecken haben Sie gesehen? ")
    polynr = checkeck(polyin)
    while not polynr:
        polyin = input("Bitte gib eine natürliche Zahl zwischen 3 und 10 ein! ")
        polynr = checkeck(polyin)
    if polynr:
        polyside = input("Mal angenommen das Alien hat wirklich " + polyin +" Ecken...zwischen 1-100, wie gross würden Sie eine Seite einschätzen? ")
        polysidenr = checkgröss(polyside)
    while not polysidenr:
        print("Bitte gib eine natürliche Zahl zwischen 1 und 100 ein!")
        polyside = input("Wie gross ist die Seite? ")
        polysidenr = checkgröss(polyside)
    cheese = input("Nebenbei, auf einer Skala von 1 bis 10, wie sehr magst du Käse? ")
    cheese = checkoneten(cheese)
    while not cheese:
        print("Bitte Gib eine Zahl zwischen 1-10 ein!")
        cheese = input("Wie sehr magst du Käse? ")
        cheese = checkoneten(cheese)
    drawpolygon_kopf(polyin, polyside, cheese)
