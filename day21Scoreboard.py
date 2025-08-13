from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1Score = 0
        self.computerScore = 0
        self.write(f"{self.p1Score} -- {self.computerScore}",True,"center",("Arial" ,20,"bold"))