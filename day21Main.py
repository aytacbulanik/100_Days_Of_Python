from turtle import Screen
from day21paddle import Paddle
from day21Ball import Ball
from day21Scoreboard import Scoreboard
import time

p1paddle = Paddle(-350)
computerPaddle = Paddle(350)
ball = Ball()
screen = Screen()
scoreBoard = Scoreboard()
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
    time.sleep(0.07)
    screen.update()
    ball.move()
    #topun üst yada alt tarafa çarptığını kontrol ediyoruz. 
    # y değerini arttırma ve azalatma yapıyoruz.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    #topuun sağ paddle çarpmasını kontrol ediyoruz.
    if ball.distance(computerPaddle) < 50 and ball.xcor() > 320 or ball.distance(p1paddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    #topun player için sayı olduğunu kontrol edeceğiz.
    if ball.xcor() > 380:
        ball.resetBall()
        scoreBoard.upP1Score()
    #topun computer için sayı olduğunu kontrol edeceğiz.
    if ball.xcor() < -380:
        ball.resetBall()
        scoreBoard.upComputerScore()



screen.exitonclick()