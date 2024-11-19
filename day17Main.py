from day17Data import question_data
from day17QuestionModel import Question
from day17QuizBrain import QuizBrain


questionBank = []

for question in question_data:
    qText = question["text"]
    qAnswer = question["answer"]
    newQuestion = Question(qText,qAnswer)
    questionBank.append(newQuestion)

newQuiz = QuizBrain(questionBank)
print(newQuiz.nextQuestion())