from tkinter import * 

window = Tk()
window.title("My First GUI Program") 
window.minsize(width=500,height=300)
window.config(padx=40,pady=50) #ana ekrana padding vermek için kullanılır
myLabel = Label(text="New Text",font=("Arial",20,"bold"))
myLabel.grid(column=0,row=0)
myLabel.config(padx=50,pady=10) #widget lara özel padding vermek için bu yöntem kullanılır.

def clickedButton():
    print("buton Clicked")
myButton = Button(text="Click Me" , command=clickedButton)
myButton.grid(column=1,row=1)


myButton2 = Button(text="Click Me" , command=clickedButton)
myButton2.grid(column=3,row=0)

myInput = Entry()
myInput.grid(column=4,row=3)
window.mainloop()