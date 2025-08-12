from day17Data import question_data
from day17QuestionModel import Question
from day17QuizBrain import QuizBrain


questionBank = []

for question in question_data["results"]:
    qText = question["question"]
    qAnswer = question["correct_answer"]
    newQuestion = Question(qText,qAnswer)
    questionBank.append(newQuestion)

newQuiz = QuizBrain(questionBank)

while newQuiz.controlQuizEnd():
    newQuiz.nextQuestion()

print("Your quiz is completed")
print(f"Your final Score : {newQuiz.score}")