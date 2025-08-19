from turtle import Screen
from day23Player import Player
from day23CarManager import CarManager
import time

screen = Screen()
player = Player()
carManager = CarManager()

screen.setup(600,600)
screen.listen()
screen.tracer(0)

screen.onkey(player.moveUp ,"Up")
screen.onkey(player.moveDown , "Down")


gameIsOn = True
while gameIsOn:
    time.sleep(0.05)
    screen.update()
    carManager.carMove()


screen.exitonclick()