from turtle import Screen
from day21paddle import Paddle

p1paddle = Paddle(-350)
computerPaddle = Paddle(350)
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.listen()
screen.tracer(0)

screen.onkey(p1paddle.moveUp,"w")
screen.onkey(p1paddle.moveDown,"s")
screen.onkey(computerPaddle.moveUp,"Up")
screen.onkey(computerPaddle.moveDown,"Down")

gameIsOn = True
while gameIsOn:
    screen.update()


screen.exitonclick()