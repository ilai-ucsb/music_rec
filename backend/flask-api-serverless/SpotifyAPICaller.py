import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'ea21fe594d6342c4b5d33990b7315a26'
secret = '0406ab09cc844180a2b79cebe7f328ed'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def top_tracks(artist):
    track_name = []
    raw_data = sp.search(q="artist:" + artist, type='track', limit=1)
    artist_id = raw_data['tracks']['items'][0]['artists'][0]['id']
    track_list = sp.artist_top_tracks(artist_id=artist_id)
    for i in range(5):
        track_name.append(track_list['tracks'][i]['name'])

    return track_name