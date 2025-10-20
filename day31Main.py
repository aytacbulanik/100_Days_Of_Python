import pandas
from random import randint
from tkinter import *

data = pandas.read_csv("./files/test.csv")
def newQuestion():
    englishDict = data["english"].to_dict()
    turkishDict = data["turkish"].to_dict()
    question = randint(0,10)
    english = englishDict[question]
    turkish = turkishDict[question]
    return (english,turkish)

window = Tk()
window.title("Flashy")
window.config(padx=40,pady=40)
bgImagePath = "./files/day31/card_back.png"
trueButtonPath = "./files/day31/right.png"
falseButtonPath = "./files/day31/wrong.png"
bgImage = PhotoImage(file=bgImagePath)
trueImage = PhotoImage(file=trueButtonPath)
falseImage = PhotoImage(file=falseButtonPath)
canvas = Canvas(width=800,height=600,bg="white",highlightthickness=0)
canvas.create_image(400,300,image=bgImage)
canvas.grid(row=0,column=0,columnspan=2)

trueButton = Button(image=trueImage,highlightthickness=0)
trueButton.grid(row=1,column=0)

falseButton = Button(image=falseImage,highlightthickness=0)
falseButton.grid(row=1,column=1)





window.mainloop()