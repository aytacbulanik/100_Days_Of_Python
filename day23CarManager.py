from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.createCar()

    def createCar(self):
        self.shape("square")
        self.penup()
        self.shapesize(1,2)
        self.color("red")
        self.hideturtle()
        self.goto(200,0)
        self.showturtle()

    def carMove(self):
        newX = self.xcor() - 10
        newY = self.ycor()
        self.goto(newX,newY)