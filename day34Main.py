from day34Data import questions
from tkinter import *
from day34UI import QuizUI
from day34QuizBrain import QuizBrain

quizBrain = QuizBrain(questions)
quizUi = QuizUI(quizBrain=quizBrain)



