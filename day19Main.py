from turtle import Turtle , Screen
import random

myScreen = Screen()
gameIsOn = True
colors = ["red" , "orange" , "yellow" , "green" , "purple" ,"brown"]
yPozisiton = [-70 ,-40,-10,20,50,80]
myTrutles = []
myScreen.setup(width=500 , height=400)
userChoose = myScreen.textinput(title="Who is win" , prompt="please enter your bet ?")

for index in range(0,6):
    newTurtle = Turtle("turtle")
    newTurtle.penup()
    newTurtle.color(colors[index])
    newTurtle.goto(-230 , yPozisiton[index])
    myTrutles.append(newTurtle)

while gameIsOn:
    for turtle in myTrutles:
        randomMove = random.randint(0,10)
        turtle.forward(randomMove)
        if turtle.xcor() == 220:
            gameIsOn = False
            if userChoose == turtle.color()[0]:
                print("You win")
            else:
                print("You lose")
myScreen.exitonclick()