from turtle import Turtle , Screen
import random

myTuppleArray = [(101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 120, 240), (56, 179, 154), (49, 124, 170)]

myTurtle = Turtle()
myScreen = Screen()
myScreen.colormode(255)
myXPostion = -400
myYPosition = -300
myTurtle.shape("arrow") #hangi şekli seçeceğimizi bu kodla belirliyoruz
myTurtle.pensize(1) # şeklin kalınlığını belirliyor
myTurtle.speed("fast") #şeklin hızını belirliyoruz

def randomColor():
    newColor = random.choice(myTuppleArray)
    return newColor
print(myScreen.screensize())
myTurtle.penup()
myTurtle.hideturtle()
myTurtle.setposition(myXPostion,myYPosition)
def randomWalk():
    myTurtle.color(randomColor())
    myTurtle.dot(20)
     #şekle oluşturduğumuz fonksiyon ile karışık renk veriyoruz.
    myTurtle.forward(70)
for _ in range(10):    
    for _ in range(10):
        randomWalk()
    myXPostion = -400
    myYPosition += 50
    myTurtle.setposition(myXPostion,myYPosition)

myScreen.exitonclick()