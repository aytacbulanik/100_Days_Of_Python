class QuizBrain:

    def __init__(self,questionList):
        self.qustionNumber = 0
        self.score = 0
        self.questionList = questionList
        self.currentQuestion = None
        
    def nextQuestion(self):
        self.currentQuestion = self.questionList[self.qustionNumber]
        self.qustionNumber += 1
        question = self.currentQuestion.question
        return f"Q.{self.qustionNumber} : {question}"