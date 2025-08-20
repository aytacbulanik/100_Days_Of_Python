from turtle import Screen
from day23Player import Player
from day23CarManager import CarManager
from day23Scoreboard import Scoreboard
import time

screen = Screen()
player = Player()
carManager = CarManager()
scoreBoard = Scoreboard()

screen.setup(600,600)
screen.listen()
screen.tracer(0)

screen.onkey(player.moveUp ,"Up")

gameIsOn = True
while gameIsOn:
    time.sleep(scoreBoard.levelSpeed)
    screen.update()
    carManager.createCar()
    carManager.carMove()
    
    #detected level completed
    if player.ycor() > 300:
        player.update()
        scoreBoard.increaseLevel()

    #detected crash car
    for oneCar in carManager.allCars:
        if player.distance(oneCar) < 10:
            scoreBoard.endGame()
            gameIsOn = False


screen.exitonclick()