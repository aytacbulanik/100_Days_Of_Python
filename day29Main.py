from tkinter import *
from tkinter import messagebox #uyarı mesajlarını kullanmak için bunu dahil etmemiz lazım
from random import randint , choice , shuffle #bu şekilde yazılınca her fonksiyon başında
#random yazmadan da kullanabiliriz.
import json

def generatePassword():
    passwordEntry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    #aşağıda list comparation kullanarak yeni diziler elde ettik
    paswordLetters = [choice(letters) for _ in range(randint(8,10))]
    paswordSymbols = [choice(numbers) for _ in range(randint(2,4))]
    paswordNumbers = [choice(symbols) for _ in range(randint(2,4))]
    #bunlarla yeni tek list elde edip bunu karıştırdık
    paswordLists = paswordLetters + paswordSymbols + paswordNumbers
    shuffle(paswordLists)

    password = "".join(paswordLists) #join metodu bir listedeki elemanları sona ekliyor.
    passwordEntry.insert(0,password)
def search():
    website = websiteEntry.get()
    
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
logoPath = "./images/passwordLogo.png"
passwordImage = PhotoImage(file=logoPath)
canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0)
canvas.create_image(100,100,image=passwordImage)
canvas.grid(column=1,row=0)

label1 = Label(text="Website : ")
label1.grid(row=1,column=0)

websiteEntry = Entry(width=31)
websiteEntry.grid(row=1,column=1) #grid yönteminde 
#columnspan değeri kaç colon boyunca uzaması gerektiğini ayarlıyor.
websiteEntry.focus() #imlecin direk burada başlamasını sağlıyor.

label2 = Label(text="E-mail / Username : ")
label2.grid(row=2,column=0)

emailEntry = Entry(width=50)
emailEntry.grid(row=2,column=1,columnspan=2)
#alana direk veri yazmak istiyorsak insert kullanılır. 0 verirsek en başa yazar
#END kullanırsak en sona ekler.veriyi str olarak göndeririz.
emailEntry.insert(0,"aytacbulanik@hotmail.com")

label3 = Label(text="Password : ")
label3.grid(row=3,column=0)

passwordEntry = Entry(width=31)
passwordEntry.grid(row=3,column=1)

def writeData():
    websiteText = websiteEntry.get()
    emailText = emailEntry.get()
    passwordText = passwordEntry.get()
    newData = {
        websiteText : {
            "email" : emailText,
            "password" : passwordText
            }
        }

    #alanlar boş mu kontrolü yapıyoruz.
    if len(websiteText) < 1 or len(passwordText) < 1:
        messagebox.showinfo(title="Hata !!!",message="Alanlar boş olamaz")
    else:
        try:
            #bu kod bloğu ile veriyi alıp güncelleiyoruz.
            with open("./files/jsonData.json",mode="r") as dataFile:
                data = json.load(dataFile) 
        except FileNotFoundError:
            with open("./files/jsonData.json",mode="w") as dataFile:
                json.dump(newData,dataFile,indent=4)
        except json.decoder.JSONDecodeError :
            with open("./files/jsonData.json",mode="w") as dataFile:
                json.dump(newData,dataFile,indent=4)
        else:
            data.update(newData)
            #bu kod bloğu ile dosyadaki herşeyi silip eski veriyle birlikte güncellennen yeni veriyi yazıyoruz.
            with open("./files/jsonData.json",mode="w") as dataFile:
                json.dump(data,dataFile,indent=4)
        finally:
            websiteEntry.delete(0,END)
            passwordEntry.delete(0,END)

generateButton = Button(text="Generate Password",width=14,command=generatePassword)
generateButton.grid(row=3,column=2)

searchButton = Button(text="Search",width=14,command=search)
searchButton.grid(row=1,column=2)

addButton = Button(text="Add",width=42,command=writeData)
addButton.grid(row=4,column=1,columnspan=2)

window.mainloop()