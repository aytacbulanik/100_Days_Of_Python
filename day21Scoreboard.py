from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1Score = 0
        self.computerScore = 0
        self.updateScoreboard()
        
#score değiştiğinde genel scoreboard ı güncelliyor.
    def updateScoreboard(self):
        self.clear()
        self.goto(0,260)
        self.write(f"{self.p1Score} -- {self.computerScore}",True,"center",("Arial" ,30,"bold"))
#oyuncunun score unu arttırıyor.
    def upP1Score(self):
        self.p1Score += 1
        self.updateScoreboard()
#oyuncunun score unu arttırıyor.
    def upComputerScore(self):
        self.computerScore += 1
        self.updateScoreboard()