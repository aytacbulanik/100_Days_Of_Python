import turtle as t
import random
xcor = -300
ycor = 0
myScreen = t.Screen()
tim = t.Turtle()
tim.pensize(1)
tim.speed(15)
tim.penup()
tim.hideturtle()
tim.setx(-300)
def randomColor():
    return (random.random() , random.random() , random.random())
def randomMove(number):
    tim.pencolor(randomColor())
    tim.dot(20)
    tim.forward(50)
    


for i in range(10):
    for _ in range(10):
        randomMove(i)
    ycor += 40
    tim.sety(ycor)
    tim.setx(-300)
myScreen.exitonclick()

