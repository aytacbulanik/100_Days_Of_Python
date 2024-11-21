from turtle import Turtle , Screen

myTurtle = Turtle()
myScreen = Screen()
myTurtle.shape("arrow")
myTurtle.color(0.4,0.8,0.9)
kenarSayisi = 3
donusAcisi = 360 / kenarSayisi
for _ in range(5):
    for _ in range(kenarSayisi):
        myTurtle.forward(50)
        myTurtle.right(donusAcisi)
    kenarSayisi += 1
myScreen.exitonclick()