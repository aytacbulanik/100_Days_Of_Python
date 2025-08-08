from turtle import Turtle
#Uygulamadaki sabitleri belirttik
MYPOSITIONS = [(0,0) , (-20 , 0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVEDISTANCE = 20


class Snake:
      
    def __init__(self):
        self.mySegments = []
        self.createSnake()
        self.head = self.mySegments[0]
    #snake in parçalarını eklemek için bu fonksiyonu kullanıyoruz.
    def createSnake(self):    
        for position in MYPOSITIONS:
            self.addSegment(position)
    
    def addSegment(self,position):
        newSegment = Turtle("square")
        newSegment.color("white")
        newSegment.penup()
        newSegment.goto(position)
        self.mySegments.append(newSegment)
    #bir tane yem yediğinde uzatmak için kullanıyoruz.
    def extend(self):
        self.addSegment(self.mySegments[-1].position())
        
    #aşağıdaki for loop son elemanı alıyor ve onun yeni koordinatına ondan bir öncekinin koordinatını atıyor. 
    # böyle tüm koordinarları yeniliyor. sonra da ilk elemana hareket veriliyor.
    def move(self):
        for seg_num in range(len(self.mySegments)-1,0,-1):
            newX = self.mySegments[seg_num - 1].xcor()
            newY = self.mySegments[seg_num - 1].ycor()
            self.mySegments[seg_num].goto(newX,newY)
        self.head.forward(MOVEDISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN: #gittiği yönün tam tersi yönde gitmesin diye bu kontrolü ekliyoruz.
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

