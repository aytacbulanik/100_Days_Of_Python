class QuizBrain:

    def __init__(self,questionList):
        self.qustionNumber = 0
        self.score = 0
        self.questionList = questionList
        self.currentQuestion = None
        
    def isStillHasQuestions(self) -> bool:
        return self.qustionNumber < len(self.questionList)
    
    def nextQuestion(self):
        self.currentQuestion = self.questionList[self.qustionNumber]
        self.qustionNumber += 1
        question = self.currentQuestion.question
        return f"Q.{self.qustionNumber} : {question}"
    
    def checkAnswer(self,userAnswer : str) -> bool:
        correctAnswer : str = self.currentQuestion.answer
        if userAnswer.upper() == correctAnswer.upper():
            return True
        else:
            return False