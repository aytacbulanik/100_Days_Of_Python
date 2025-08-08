class Question:
    def __init__(self,text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:
    def __init__(self,questionList):
        self.questionList = questionList
        self.questionNumber = 0
        self.score = 0
    
    def getNewQuestion(self):
        
        self.questionNumber += 1
        

    def stillHasQuestion(self):
        if len(self.questionList) <= self.questionNumber:
            return False
        else:
            return True
        
    def checkAnswer(self):
        currentQuestion = self.questionList[self.questionNumber]
        yourAnswer = input(f"Q.{self.questionNumber} : {currentQuestion.text} (True/False)?: ")
        if self.questionList[self.questionNumber].answer.lower() == yourAnswer.lower():
            self.score += 1
            print(f"Cong ! Your answer is true. Score : {self.score} / ")
        else:
            print(f"Your answer is false. Score : {self.score} / {self.questionNumber + 1}")