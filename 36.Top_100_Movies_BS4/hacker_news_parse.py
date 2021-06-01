from bs4 import BeautifulSoup
import requests

# Parsing Hacker News site to get the HTML Data

response = requests.get("https://news.ycombinator.com/")
yc_page = response.text
soup = BeautifulSoup(yc_page, "html.parser")

article_votes = []
article_texts = []
article_links = []

# Parsing HTML with Soup to get Article Links and Title

article_data = soup.findAll(name="a", class_="storylink")
article_vote_data = [
    int(score.getText().split()[0])
    for score in soup.findAll(name="span", class_="score")
]

# Storing Data in List and checking the article with Highest Votes

for data in article_data:
    text = data.getText()
    article_texts.append(text)
    link = data.get("href")
    article_links.append(link)

max_vote = max(article_vote_data)
print(article_texts[article_vote_data.index(max_vote)])
print(article_links[article_vote_data.index(max_vote)])
print(max_vote)
