import requests 
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text)

questions = soup.select(".question-summary", "html.parser")
print(type(questions))