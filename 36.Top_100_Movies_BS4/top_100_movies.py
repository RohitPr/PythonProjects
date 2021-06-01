from bs4 import BeautifulSoup
import requests

SHEETY_API = "https://api.sheety.co/f0b2e84905e64f22023d297978a9331c/movies/movies"

response = requests.get(
    "https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century"
)

movie_page = response.text

soup = BeautifulSoup(movie_page, "lxml")

select = "section > div > div > div > main > main > div > div > h2 > strong "

movie_data = soup.select(select)

movie_names = [movie.getText() for movie in movie_data]

for item in movie_names:
    print(item)
    movie_input = {"movies": {"movies": item}}
    response = requests.post(url=SHEETY_API, json=movie_input)
    print(response.status_code)
