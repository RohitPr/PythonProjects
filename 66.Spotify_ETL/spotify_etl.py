import json
import datetime
from datetime import datetime, timedelta
import requests
import sqlite3
import sqlite3
import sqlalchemy
from sqlalchemy.orm import sessionmaker

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "v5gqmoefaafptlgwxtbqasude"
TOKEN = "BQABeiAEQH0WAyY4bESu4sXqb2m1Q-pyf4ewGwZ8Vo3oGwhodFRL91y0pP9JNAfEaG_DKlOr_2NheJstXGbRq4IWXWCqifCoSwtAUfot7NRh1zYOf8cqw5YuF-HRjI0sJASdYO5hbQ-0YFB-cf6g4zGceaJPMV3Ir4Hv"

if __name__ == "__main__":
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }

today = datetime.now()
yesterday = today - timedelta(days=1)
yesterday_timestamp = int(yesterday.timestamp()) * 1000

spotify_request = requests.get(
    "https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_timestamp), headers=headers)

spotify_data = spotify_request.json()
print(spotify_data)
