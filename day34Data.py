import requests
from day34QuestionModel import QuestionModel
import html

paramaters = {
    "amount" : 10,
    "type" : "boolean"
}
response = requests.get(url="https://opentdb.com/api.php",params=paramaters)
response.raise_for_status()
data = response.json()["results"]
questions = []
for quest in data:
    question = html.unescape(quest["question"])
    correctAnswer = quest["correct_answer"]
    newQuestion = QuestionModel(question=question,answer=correctAnswer)
    questions.append(newQuestion)
