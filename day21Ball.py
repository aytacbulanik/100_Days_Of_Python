from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.yMove = 10
        self.xMove = 10
    #sürekli 10 birim ekleyerek ilerliyor.
    def move(self):
        newX = self.xcor() + self.xMove
        newY = self.ycor() + self.yMove
        self.goto(newX , newY)

    #y coordinatında simetriğini alıyor
    def bounceY(self):
        self.yMove *= -1

    #x coordinatında simetriğini alıyor.
    def bounceX(self):
        self.xMove *= -1

    def resetBall(self):
        self.goto(0,0)
        self.bounceX()