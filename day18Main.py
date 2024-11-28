from turtle import Turtle , Screen
import random


myTurtle = Turtle()
myScreen = Screen()
myScreen.colormode(255)

myTurtle.shape("arrow") #hangi şekli seçeceğimizi bu kodla belirliyoruz
myTurtle.pensize(8) # şeklin kalınlığını belirliyor
myTurtle.speed("fast") #şeklin hızını belirliyoruz
colorList = ["dark orange","deep sky blue","forest green","medium violet red"]
angleList = [0,90,180,270]

def randomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red, green , blue)
def randomWalk():
    myTurtle.forward(30) #kaç birim ilerleyeceğimizi belirliyoruz
    myTurtle.setheading(random.choice(angleList)) #şeklin dönüş yönünü listeden seçerek belirliyoruz
    myTurtle.color(randomColor()) #şekle oluşturduğumuz fonksiyon ile karışık renk veriyoruz.
for _ in range(100):
    randomWalk()
myScreen.exitonclick()