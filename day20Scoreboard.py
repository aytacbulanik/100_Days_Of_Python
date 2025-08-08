from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.refresh()
        

    def increcise(self):
        self.score += 1
        self.refresh()

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER",True,align="center",font=("Arial",10,"bold"))

    def refresh(self):
        self.clear()
        self.goto(0,280)
        self.color("white")
        self.write(f"Score : {self.score}",True,align="center",font=("Arial",10,"bold"))