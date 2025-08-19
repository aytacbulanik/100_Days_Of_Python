from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def moveUp(self):
        newX = self.xcor()
        newY = self.ycor() + 20
        self.goto(newX,newY)

    def moveDown(self):
        newX = self.xcor()
        if self.ycor() > -280:
            newY = self.ycor() - 20
            self.goto(newX,newY)