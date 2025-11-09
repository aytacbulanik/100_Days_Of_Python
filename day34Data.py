import requests
from day34QuestionModel import QuestionModel

paramaters = {
    "amount" : 10,
    "type" : "boolean"
}
response = requests.get(url="https://opentdb.com/api.php",params=paramaters)
response.raise_for_status()
data = response.json()["results"]
questions = []
print(data)
for quest in data:
    question = quest["question"]
    correctAnswer = quest["correct_answer"]
    newQuestion = QuestionModel(question=question,answer=correctAnswer)
    questions.append(newQuestion)