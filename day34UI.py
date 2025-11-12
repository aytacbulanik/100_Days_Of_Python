from tkinter import *
from day34QuizBrain import QuizBrain

ThemeColor = "#375362"

class QuizUI:
    
    def __init__(self , quizBrain : QuizBrain):
        self.window = Tk()
        self.quiz = quizBrain
        self.window.title("Trivia Question Game")
        self.window.config(padx=30,pady=30,bg=ThemeColor)

        self.scoreText = Label(text="Score : 0",highlightthickness=0,fg="white", bg=ThemeColor,font=("Arial",12))
        self.scoreText.grid(column=1,row=0)
        self.scoreText.config(pady=10)

        self.canvas = Canvas(width=300,height=250,highlightthickness=0)
        self.questionText = self.canvas.create_text(150,
                                                    125,
                                                    width=280,
                                                    text="Question Text",
                                                    font=("Arial",20)) 
        self.canvas.grid(column=0,row=1,columnspan=2,pady=30)
        trueImage = PhotoImage(file="./files/day34/true.png")
        falseImage = PhotoImage(file="./files/day34/false.png")
        self.trueButton = Button(image=trueImage,highlightthickness=0,command=self.truePressed)
        self.trueButton.grid(column=0,row=2)

        self.falseButton = Button(image=falseImage,highlightthickness=0,command=self.falsePressed)
        self.falseButton.grid(column=1,row=2)
        self.showNextQuestion()
        self.window.mainloop()

    def showNextQuestion(self):
        self.canvas.config(bg="white")
        if self.quiz.isStillHasQuestions():
            self.canvas.itemconfig(self.questionText,text=self.quiz.nextQuestion())
        else:
            self.canvas.itemconfig(self.questionText,text="TEST BİTTİ")
            self.falseButton.config(state="disabled")
            self.trueButton.config(state="disabled")

    def truePressed(self):
        result = self.quiz.checkAnswer("True")
        self.getFeedback(result)
    
    def falsePressed(self):
        result = self.quiz.checkAnswer("False")
        self.getFeedback(result)

    def getFeedback(self,isRight):
        if isRight:
            self.quiz.score += 1
            self.scoreText.config(text=f"Score : {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.scoreText.config(text=f"Score : {self.quiz.score}")
            self.canvas.config(bg="red")
        self.window.after(1000,self.showNextQuestion)
