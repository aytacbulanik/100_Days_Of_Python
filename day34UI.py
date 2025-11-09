from tkinter import *

ThemeColor = "#375362"

class QuizUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Trivia Question Game")
        self.window.config(padx=30,pady=30,bg=ThemeColor)

        self.scoreText = Label(text="Score : 0",highlightthickness=0,fg="white", bg=ThemeColor,font=("Arial",12))
        self.scoreText.grid(column=1,row=0)
        self.scoreText.config(pady=10)

        self.canvas = Canvas(width=300,height=250,highlightthickness=0)
        self.questionText = self.canvas.create_text(150,125,text="Question Text",font=("Arial",20)) 
        self.canvas.grid(column=0,row=1,columnspan=2,pady=30)
        trueImage = PhotoImage(file="./files/day34/true.png")
        falseImage = PhotoImage(file="./files/day34/false.png")
        self.trueButton = Button(image=trueImage,highlightthickness=0)
        self.trueButton.grid(column=0,row=2)

        self.falseButton = Button(image=falseImage,highlightthickness=0)
        self.falseButton.grid(column=1,row=2)

        self.window.mainloop()