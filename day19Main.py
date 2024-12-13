from turtle import Turtle , Screen

myTurtle = Turtle()
myScreen = Screen()

def moveForward():
    myTurtle.forward(30)
def moveBackward():
    myTurtle.backward(30)
def turnClock():
    myTurtle.left(90)
def turnRightClockwise():
    myTurtle.right(70)
myScreen.listen()
myScreen.onkey(moveForward, "w")
myScreen.onkey(moveBackward, "s")
myScreen.onkey(turnClock, "a")
myScreen.onkey(turnRightClockwise, "d")
myScreen.exitonclick()