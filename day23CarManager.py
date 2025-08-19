from turtle import Turtle
import random

class CarManager:
    
    def __init__(self):
        super().__init__()
        self.allCars = []

    def createCar(self):
        randomChange = random.randint(1,6)
        if randomChange == 1:
            randomY = random.randint(-260,260)
            newTurtle = Turtle()
            newTurtle.shape("square")
            newTurtle.penup()
            newTurtle.shapesize(1,2)
            newTurtle.color(self.randomColor())
            newTurtle.goto(300,randomY)
            self.allCars.append(newTurtle)

    def randomColor(self):
        return (random.random(),random.random(),random.random())
    
    def carMove(self):
        for car in self.allCars:
            car.backward(10)