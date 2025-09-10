from turtle import Turtle , Screen
import pandas

turtle = Turtle()
data = pandas.read_csv("50_states.csv")
dataListName = data["state"].to_list()
screen = Screen()
corretStates = [] #doğru cevaplar bu dizide tutuluyor
unUsedStates = [] #cevaplanmalayan cevaplar bu dizide tutuluyor
screen.title("The US State Game") #açılan ekrana başlık veriyor
image = "blank_states_img.gif" #resmi değişken olarak tanımladık.
screen.addshape(image)
turtle.shape(image) #ekran açılınca resimle aktif oluyor
gameIsOn = True
    
while gameIsOn:
    userAnswer = screen.textinput(title=f"{len(corretStates)} / 50 State name",prompt="what is the state's name ?")
    capName = str(userAnswer).title()
    #oyundan çıkmak için kontrol oluşturduk.bulamadığımız state ler diziye ekleniyor
    if capName == "Exit":
        for state in dataListName:
            if state not in corretStates:
                unUsedStates.append(state)
        break
    #verilen cevapların kontrolü sağlanıyor ve diziye ekleniyor.
    if  capName in dataListName:
        coor = data[data.state == capName]
        corretStates.append(capName)
        newturtle = Turtle()
        newturtle.hideturtle()
        newturtle.penup()
        newturtle.goto(int(coor.x),int(coor.y))
        newturtle.write(capName,True,"center",("Arial",12,"bold"))
