from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
logoPath = "passwordLogo.png"
passwordImage = PhotoImage(file=logoPath)
canvas = Canvas(width=200,height=200,bg="white",highlightthickness=0,borderwidth=3)
canvas.create_image(100,100,image=passwordImage)
canvas.grid(column=1,row=0)

label1 = Label(text="Website : ")
label1.grid(row=1,column=0)

websiteEntry = Entry(width=50)
websiteEntry.grid(row=1,column=1,columnspan=2) #grid yönteminde 
#columnspan değeri kaç colon boyunca uzaması gerektiğini ayarlıyor.
websiteEntry.focus() #imlecin direk burada başlamasını sağlıyor.

label2 = Label(text="E-mail / Username : ")
label2.grid(row=2,column=0)

emailEntry = Entry(width=50)
emailEntry.grid(row=2,column=1,columnspan=2)
#alana direk veri yazmak istiyorsak inseet kullanılır. 0 verirsek en başa yazar
#END kullanırsak en sona ekler
emailEntry.insert(0,"aytacbulanik@hotmail.com")

label3 = Label(text="Password : ")
label3.grid(row=3,column=0)

passwordEntry = Entry(width=31)
passwordEntry.grid(row=3,column=1)

def writeData():
        websiteText = websiteEntry.get()
        emailText = emailEntry.get()
        passwordText = passwordEntry.get()
        with open("./files/passwordData.txt",mode="a",encoding="utf-8")as dataFile:
            dataFile.write(f"{websiteText} : {emailText} : {passwordText}" + "\n")
        websiteEntry.delete(0,END)
        emailEntry.delete(0,END)
        passwordEntry.delete(0,END)
generateButton = Button(text="Generate Password",width=14)
generateButton.grid(row=3,column=2)

addButton = Button(text="Add",width=42,command=writeData)
addButton.grid(row=4,column=1,columnspan=2)








window.mainloop()