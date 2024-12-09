from turtle import Turtle , Screen
import random


myTurtle = Turtle()
myScreen = Screen()
myScreen.colormode(255)

myTurtle.shape("arrow") #hangi şekli seçeceğimizi bu kodla belirliyoruz
myTurtle.pensize(1) # şeklin kalınlığını belirliyor
myTurtle.speed("fastest") #şeklin hızını belirliyoruz

def randomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red, green , blue)
def upperAngle(angle):
    newAngle = angle + 5
    return newAngle
def randomWalk():
    myTurtle.circle(100)
    myTurtle.setheading(myTurtle.heading() + 5)
    
   
    myTurtle.color(randomColor()) #şekle oluşturduğumuz fonksiyon ile karışık renk veriyoruz.
for _ in range(72):
    randomWalk()
myScreen.exitonclick()