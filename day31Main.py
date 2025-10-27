import pandas
from random import choice
from tkinter import *

BGCOLOR = "#B1DDC6"
data = pandas.read_csv("./files/test.csv")
#burası çok önemli data frame de olan her bir satırı dict nesnesine çeviriyor
dataDict = data.to_dict(orient="records")
def newQuestion():
    currentWord = choice(dataDict)
    canvas.itemconfig(titleText , text = "English")
    canvas.itemconfig(questionText, text = currentWord["english"])

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BGCOLOR)
bgImagePath = "./files/day31/card_front.png"
trueButtonPath = "./files/day31/right.png"
falseButtonPath = "./files/day31/wrong.png"
bgImage = PhotoImage(file=bgImagePath)
trueImage = PhotoImage(file=trueButtonPath)
falseImage = PhotoImage(file=falseButtonPath)
canvas = Canvas(width=820,height=560,highlightthickness=0,bg=BGCOLOR)
canvas.create_image(410,280,image=bgImage)
canvas.grid(row=0,column=0,columnspan=2)

titleText = canvas.create_text(400,200,text="English",font=("Arial",30,"italic"),fill="black")
questionText = canvas.create_text(400,350,text="Word",font=("Arial",40,"bold"),fill="black")
trueButton = Button(image=trueImage,highlightthickness=0,command=newQuestion)
trueButton.grid(row=1,column=0)

falseButton = Button(image=falseImage,highlightthickness=0,command=newQuestion)
falseButton.grid(row=1,column=1)

newQuestion()



window.mainloop()