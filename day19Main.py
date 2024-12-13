from turtle import Turtle , Screen

myTurtle = Turtle()
myScreen = Screen()

def moveForward():
    myTurtle.forward(20)
def moveBackward():
    myTurtle.backward(20)
def turnClock():
    myTurtle.left(10)
def turnRightClockwise():
    myTurtle.right(10)
def clearScreen():
    myTurtle.clear()
    myTurtle.penup()
    myTurtle.setheading(0)
    myTurtle.setpos(0,0)
    myTurtle.pendown()
myScreen.listen()
myScreen.onkey(moveForward, "w")
myScreen.onkey(moveBackward, "s")
myScreen.onkey(turnClock, "a")
myScreen.onkey(turnRightClockwise, "d")
myScreen.onkey(clearScreen,"c")
myScreen.exitonclick()