from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.levelSpeed = 0.1
        self.hideturtle()
        self.penup()
        self.update()
    
    def update(self):
        self.clear()
        self.goto(-280,270)
        self.write(f"Oyun Leveli : {self.level}",True,"left",("Arial",20,"normal"))

    def increaseLevel(self):
        self.level += 1
        self.levelSpeed -= 0.01
        self.update()

    def endGame(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over",True,"center",("Arial",20,"normal"))