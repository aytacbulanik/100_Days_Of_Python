from turtle import Screen 
from day20Snake import Snake
from day20Food import Food
from day20Scoreboard import Scoreboard
import time

snake = Snake()
newFood = Food()
scoreboard = Scoreboard()
screen = Screen() #ekran nesnesi oluşturuyoruz. tüm ayarlamalrı bunun üzerinden yapacağız.
screen.setup(width=600,height=600) #ekranın boyutunu belirliyoruz.
screen.bgcolor("black") #ekranın arka plan rengini belirliyoruz
screen.title("My Snake Game") #ekranın en üstüne adını yazmak için kullanıyoruz.
screen.tracer(0) #ekranın yanilenme oranını belirliyoruz.
screen.listen() #ekranda klavye tıklamaları algılansın diyo bu fonksiyon çalıştırılır.
screen.onkey(snake.up,"Up") #klavyede bir tuşa basıldığında bunu hangi tuşun ve hangi nesnenin kullanacağını tanımlıyoruz.
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


gameIsOn = True
while gameIsOn:
    screen.update() #ekranı yenile kodunu yazıyoruz.
    time.sleep(0.1) #yenilenmeden sonra ne kadarlık bir saniye beklemesi gerektiğini yazıyoruz.
    snake.move()

    #distance metodu bir nesnenin başka bir nesneye olan uzaklığını ölçmek için kullanılıyor.
    if snake.head.distance(newFood) < 14:
        newFood.refresh()
        snake.extend()
        scoreboard.increcise()
    #duvarlara çarpmasını kontrol ediyoruz.
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
        gameIsOn = False
        scoreboard.gameOver()
    #snake in kendi parçasına çarpmasını kontrol ediyoruz.
    for segment in snake.mySegments:
        if segment == snake.head:
            pass
        #snake in her bir segmesinin ilk segmentine olan uzaklığını ölçüyoruz. 10 dan küçükse çarpmış olarak algılanıyor.
        elif snake.head.distance(segment) < 10 :
            gameIsOn = False
            scoreboard.gameOver()


screen.exitonclick()
