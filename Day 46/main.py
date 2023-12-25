# בס״ד
import os
from datetime import datetime

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy import SpotifyOAuth


# specifying data and extracting songs and singers lists
def validate_date(input_date: str) -> bool:
    """
    Function to confirm the date format.
    :param input_date: Date in string format matching "YYYY-MM-DD"
    :return: boolean whether the input is matching the desired format
    """
    try:
        # Attempt to convert the input string to a datetime object
        datetime.strptime(input_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# Get user input for the date with validation
while True:
    date = input('Which date do you want to travel to?\nType date in format: YYYY-MM-DD\n')

    if validate_date(date):
        break
    else:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

URL = f'https://www.billboard.com/charts/hot-100/{date}'

response = requests.get(url=URL)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, features='html.parser')
hits = soup.find_all(name='ul',
                     class_='lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max')
songs = [hit.find('h3').getText().strip() for hit in hits]

# connecting to Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
        client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET'),
        show_dialog=True,
        cache_path="token.txt"
    )
)
# getting user_id
user_id = sp.current_user()["id"]

# searching for songs by name and year
song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# creating playlist and adding songs from the songs_uris list
if song_uris:
    playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
else:
    print('No songs found.')
