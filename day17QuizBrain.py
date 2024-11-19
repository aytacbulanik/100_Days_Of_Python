class QuizBrain:
    def __init__(self,questionList):
        self.questionNumber = 0
        self.questionList = questionList
    
    def nextQuestion(self):
        questionObject = self.questionList[self.questionNumber]
        answer = input(f"Q. {self.questionNumber + 1}. {questionObject.text} ? (True or False) :")