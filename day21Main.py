from turtle import Screen
from day21paddle import Paddle

p1paddle = Paddle()
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.listen()

screen.onkey(p1paddle.moveUp,"Up")
screen.onkey(p1paddle.moveDown,"Down")



screen.exitonclick()