import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('SPOTIPY_CLIENT_ID'), client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'))
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def top_tracks(artist):
    track_name = []
    raw_data = sp.search(q="artist:" + artist, type='track', limit=1)
    artist_id = raw_data['tracks']['items'][0]['artists'][0]['id']
    track_list = sp.artist_top_tracks(artist_id=artist_id)
    for i in range(5):
        track_name.append(track_list['tracks'][i]['name'])

    return track_name