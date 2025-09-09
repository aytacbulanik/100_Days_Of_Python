from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__(shape= "circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) #20x20 byoutlarda oluşan her bir 
        #turtle nesnesinin kaç katında oluşacağını belirtiyor.
        self.color("blue")
        self.speed("fastest")
        self.refresh()
     #bu fonksiyon snake ve food birbirine temas edince food konumunu yenilesin diye yazıldı.   
    def refresh(self):
        randomX = random.randint(-280 , 280)
        randomY = random.randint(-280 , 280)
        self.goto(randomX,randomY)

