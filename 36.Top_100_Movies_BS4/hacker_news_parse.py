from typing import Text
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_page = response.text

soup = BeautifulSoup(yc_page, "html.parser")

article_data = []
article_votes = []
article_texts = []
article_links = []
article_votes = []

article_data = soup.findAll(name="a", class_="storylink")
article_vote_data = [
    int(score.getText().split()[0])
    for score in soup.findAll(name="span", class_="score")
]

for data in article_data:
    text = data.getText()
    article_texts.append(text)
    link = data.get("href")
    article_links.append(link)

max_vote = max(article_vote_data)
print(article_texts[article_vote_data.index(max_vote)])
print(article_links[article_vote_data.index(max_vote)])
