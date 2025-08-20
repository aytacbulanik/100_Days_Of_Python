from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = 0
        self.penup()
        self.hideturtle()
        self.refresh()
        

    def increcise(self):
        self.score += 1
        self.refresh()

    def resetGame(self):
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        self.refresh()

    #def gameOver(self):
    #   self.goto(0,0)
    #   self.write("GAME OVER",True,align="center",font=("Arial",10,"bold"))

    def refresh(self):
        self.clear()
        self.goto(0,280)
        self.color("white")
        self.write(f"Score : {self.score} - High Score : {self.highScore}",True,align="center",font=("Arial",10,"bold"))