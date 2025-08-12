from day17Data import question_data
from day17QuestionModel import Question , QuizBrain

questionBank = question_data
newQuiz = QuizBrain(questionBank)

while newQuiz.stillHasQuestion():
    newQuiz.checkAnswer()
    newQuiz.getNewQuestion()
    