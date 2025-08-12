from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,xcor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(xcor,0)

    def moveUp(self):
        newY = self.ycor() + 20
        self.sety(newY)
    
    def moveDown(self):
        newY = self.ycor() - 20
        self.sety(newY)