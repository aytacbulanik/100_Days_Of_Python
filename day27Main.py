from tkinter import * 

window = Tk()
window.title("My First GUI Program") 
window.minsize(width=200,height=100)
window.config(padx=30,pady=30)

myEntry = Entry()
myEntry.grid(column=1,row=0)

myLabel1 = Label(text="is equal to ")
myLabel1.grid(column=0,row=1)

myLabel2 = Label(text="Miles")
myLabel2.grid(column=2,row=0)

myLabel3 = Label(text="0")
myLabel3.grid(column=1,row=1)

myLabel4 = Label(text="Km")
myLabel4.grid(column=2,row=1)

def calculate():
    myMile = float(myEntry.get())
    myKm = int(myMile * 1.6)
    myLabel3.config(text=str(myKm))

myButton = Button(text="Calculate" , command=calculate)
myButton.grid(column=1,row=2)


window.mainloop()