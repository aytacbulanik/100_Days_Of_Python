from turtle import Turtle , Screen
import random
import colorgram

myTuppleArray = []

myColor = colorgram.extract("cologram.jpg",7)
for color in myColor:
    newTupple = (color.rgb.r,color.rgb.g,color.rgb.b)
    myTuppleArray.append(newTupple)
print(myTuppleArray[0])
myTurtle = Turtle()
myScreen = Screen()
myScreen.colormode(255)

myTurtle.shape("arrow") #hangi şekli seçeceğimizi bu kodla belirliyoruz
myTurtle.pensize(1) # şeklin kalınlığını belirliyor
myTurtle.speed("fastest") #şeklin hızını belirliyoruz

def randomColor():
    newColor = random.choice(myTuppleArray)
    return newColor

def randomWalk():
    myTurtle.circle(100)
    myTurtle.setheading(myTurtle.heading() + 10)
    myTurtle.color(randomColor()) #şekle oluşturduğumuz fonksiyon ile karışık renk veriyoruz.
for _ in range(36):
    randomWalk()
myScreen.exitonclick()