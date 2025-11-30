from bs4 import BeautifulSoup
import requests

rateArray = []
nameArray = []
linkArray = []

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")
scoreSpan = soup.find_all(name="span" , class_="score") 
titleSpan = soup.find_all(name="span" , class_="titleline")

for title in scoreSpan:
    point = title.getText().split()[0]
    rateArray.append(int(point))

for title in titleSpan:
    nameArray.append(title.getText())
    linkArray.append(title.a['href'])

maxRate = max(rateArray)
maxIndex = rateArray.index(maxRate)
print(f"Title: {nameArray[maxIndex]}")
print(f"Link: {linkArray[maxIndex]}")

