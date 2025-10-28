import pandas
from random import choice
from tkinter import *

BGCOLOR = "#B1DDC6"
currentCard = {} #uygulamada o an gösterilen nesneyi başka boş şekilde global
#olarka tanımlıyoruz. sonra sürekli erişmek için
dataDict = {} #bunu global olarak tanımlıyoruzki başka değerde atıyalım

#aşağıda try except yapısıyla kalan kelimelerle olan dosya okunuyor
#yoksa bu dosya sıfırdan oluşturuluyor.böylece hata alınmıyor.
try:
    data = pandas.read_csv("./files/day31/newWord.csv")
except FileNotFoundError:
    originalData = pandas.read_csv("./files/day31/englishToTurkish1000.csv")
    dataDict = originalData.to_dict(orient="records")
else:
    #burası çok önemli data frame de olan her bir satırı dict nesnesine çeviriyor
    dataDict = data.to_dict(orient="records") 

def nextCard():
    global currentCard , flipTimer
    window.after_cancel(flipTimer) #her yeni card yüklendiğinde süreyi sıfırlıyor
    currentCard = choice(dataDict) #karışık kelime seçiyor.
    canvas.itemconfig(titleText , text = "English", fill="white")
    canvas.itemconfig(questionText, text = currentCard["english"], fill= "white")
    canvas.itemconfig(cardBG, image=bgImage)
    flipTimer = window.after(3000,func=changeCard) #3 saniye sonra ekranı güncelliyor

def changeCard():
    canvas.itemconfig(titleText , text= "Turkish", fill="black")
    canvas.itemconfig(questionText , text = currentCard["turkish"],fill="black")
    canvas.itemconfig(cardBG, image=bgFrontImage)

def isTrue():
    dataDict.remove(currentCard) #o anki nesneyi mevcur listeden siliyor.
    data = pandas.DataFrame(dataDict)
    data.to_csv("files/day31/newWord.csv",index=False) #bu satır çok öenmli 
    #index parametresi yeni bir csv oluştururken başına sıra numarası eklemiyor.
    nextCard()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BGCOLOR) #padx pady her yerden boşluk bırakıyor.

flipTimer = window.after(3000,func=changeCard) #uygulama ilk açıldığında 3 saniye ile kartı yeniliyor.
bgImagePath = "./files/day31/card_back.png"
bgFrontImagePath = "./files/day31/card_front.png"
trueButtonPath = "./files/day31/right.png"
falseButtonPath = "./files/day31/wrong.png"
bgImage = PhotoImage(file=bgImagePath)
bgFrontImage = PhotoImage(file=bgFrontImagePath)
trueImage = PhotoImage(file=trueButtonPath)
falseImage = PhotoImage(file=falseButtonPath)
canvas = Canvas(width=800,height=560,highlightthickness=0,bg=BGCOLOR)
cardBG = canvas.create_image(400,280,image=bgImage)
canvas.grid(row=0,column=0,columnspan=2)

titleText = canvas.create_text(400,200,text="English",font=("Arial",30,"italic"),fill="black")
questionText = canvas.create_text(400,350,text="Word",font=("Arial",40,"bold"),fill="black")
trueButton = Button(image=trueImage,highlightthickness=0,command=isTrue)
trueButton.grid(row=1,column=0)

falseButton = Button(image=falseImage,highlightthickness=0,command=nextCard)
falseButton.grid(row=1,column=1)

nextCard() #uygulama ilk açıldığında ilk kartı yüklüyor.

window.mainloop()