from day17Data import question_data
from day17QuestionModel import Question

questionBank = []

for question in question_data:
    qText = question["text"]
    qAnswer = question["answer"]
    newQuestion = Question(qText,qAnswer)
    questionBank.append(newQuestion)

print(questionBank[3].text)