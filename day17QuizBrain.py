class QuizBrain:
    def __init__(self,questionList):
        self.questionNumber = 0
        self.questionList = questionList
        
    def controlQuizEnd(self):
        return self.questionNumber < len(self.questionList)

    def nextQuestion(self):
        questionObject = self.questionList[self.questionNumber]
        answer = input(f"Q. {self.questionNumber + 1}. {questionObject.text} ? (True or False) :")
        self.questionNumber += 1