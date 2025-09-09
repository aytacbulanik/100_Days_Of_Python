from turtle import Turtle , Screen
import pandas

turtle = Turtle()
data = pandas.read_csv("50_states.csv")
dataListName = data["state"].to_list()
screen = Screen()
corretStates = [] 
screen.title("The US State Game") #açılan ekrana başlık veriyor
image = "blank_states_img.gif" #resmi değişken olarak tanımladık.
screen.addshape(image)
turtle.shape(image) #ekran açılınca resimle aktif oluyor
gameIsOn = True
def getStateCoor(name):
    capName = str(name).title()
    if  capName in dataListName:
        coor = data[data.state == capName]
        corretStates.append(capName)
        newturtle = Turtle()
        newturtle.hideturtle()
        newturtle.penup()
        newturtle.goto(int(coor.x),int(coor.y))
        newturtle.write(capName,True,"center",("Arial",12,"bold"))
while gameIsOn:
    userAnswer = screen.textinput(title=f"{len(corretStates)} / 50 State name",prompt="what is the state's name ?")
    getStateCoor(userAnswer)


screen.exitonclick()















# x ve y coordinatı alan bir fonk oluşturduk
# def getMouseClickCoor(x,y):
#     print(x,y)

#turtle.onscreenclick(getMouseClickCoor) #bu metod ekranda tıklanan coor almaya yarıyor
#turtle.mainloop()#ekran kapanmadan sürekli çalışmasını sağlıyor. exitonclick() metodunun bir farklı kullanımı

#screen.exitonclick()