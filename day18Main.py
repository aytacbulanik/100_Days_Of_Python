from turtle import Turtle , Screen
import random

myTurtle = Turtle()
myScreen = Screen()
myTurtle.shape("arrow")
myTurtle.color(0.4,0.8,0.9)
kenarSayisi = 3

for _ in range(6):
    for _ in range(kenarSayisi):
        donusAcisi = 360 / kenarSayisi
        myTurtle.forward(50)
        myTurtle.right(donusAcisi)
    kenarSayisi += 1
    myTurtle.color(random.random(),random.random(),random.random())
myScreen.exitonclick()