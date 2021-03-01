from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "CLIENT_SECRET"

# Scraping Data from Billboard for top 100 Songs for Selected Date

date = input("Enter the Date(YYYY-MM-DD): ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
song_data = soup.find_all(
    name="span", class_="chart-element__information__song text--truncate color--primary"
)

song_names = [song.getText() for song in song_data]

# Initializing Spotipy Module with My ID

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]

# Finding Track URI's and Searching Spotify for top 100 songs on Selected Date

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating Spotify Playlist with the Top 100 songs for the selected Date

playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False
)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)