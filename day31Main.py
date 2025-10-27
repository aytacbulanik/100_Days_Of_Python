import pandas
from random import randint
from tkinter import *

BGCOLOR = "#B1DDC6"
data = pandas.read_csv("./files/test.csv")

def newQuestion():
    englishDict = data["english"].to_dict()
    turkishDict = data["turkish"].to_dict()
    question = randint(0,99)
    english = englishDict[question]
    turkish = turkishDict[question]
    return [english,turkish]

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
canvas.create_image(420,300,image=bgImage)
canvas.grid(row=0,column=0,columnspan=2)
questionData = newQuestion()
titleText = canvas.create_text(400,200,text=f"{questionData[0]}",font=("Arial",40,"italic"),fill="black")
questionText = canvas.create_text(400,350,text=f"{questionData[1]}",font=("Arial",50,"bold"),fill="black")
trueButton = Button(image=trueImage,highlightthickness=0)
trueButton.grid(row=1,column=0)

falseButton = Button(image=falseImage,highlightthickness=0)
falseButton.grid(row=1,column=1)




window.mainloop()