from turtle import Screen
from day23Player import Player
import time

screen = Screen()
player = Player()

screen.setup(600,600)
screen.listen()
screen.onkey(player.moveUp ,"Up")
screen.onkey(player.moveDown , "Down")


gameIsOn = True


screen.exitonclick()