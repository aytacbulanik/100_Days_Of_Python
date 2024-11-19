class QuizBrain:
    def __init__(self,questionList):
        self.questionNumber = 0
        self.questionList = questionList
        self.score = 0

    def controlQuizEnd(self):
        return self.questionNumber < len(self.questionList)

    def nextQuestion(self):
        questionObject = self.questionList[self.questionNumber]
        correctAnswer = questionObject.answer
        answer = input(f"Q. {self.questionNumber + 1}. {questionObject.text} ? (True or False) : ")
        self.checkAnswer(answer , correctAnswer)
        self.questionNumber += 1

    def checkAnswer(self,answer,correctAnswer):
        if answer.lower() == correctAnswer.lower():
            self.score += 1
            print("Thats's right")
        else:
            print("Your answer is wrong")
            print(f"Correct Answer is : {correctAnswer}")
        print(f"your Score is : {self.score} / {self.questionNumber + 1} \n")
        