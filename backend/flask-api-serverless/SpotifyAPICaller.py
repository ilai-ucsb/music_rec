import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_credentials_manager = SpotifyClientCredentials(client_id=os.getenv('SPOTIPY_CLIENT_ID'), client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'))
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# code copied from model.py in order to not call spotify oauth multiple times
def base_model(artist_ids=None, genre_ids=None, track_ids=None, limit=10, country='US', **kwargs):
    """
    Get a list of recommended tracks for one to five seeds. (at least one of artist_ids,
    genre_ids, track_ids are needed)

    Args:
        artist_ids (List[str]) - a list of artist IDs, URIs, or URLs
        genre_ids (List[str]) - a list of genre IDs, URIs, or URLs
        track_ids (List[str]) - a list of track IDs, URIs, or URLs
        limit (int) - The maximum number of recommendations. Default: 10
        country (str) - An ISO 3166-1 alpha-2 country code. If provided, all results
            will be playable in this country. Default: "US"
        **kwargs (dict) - Any additional keyword arguments requested by the spotify API

    Returns:
        List - A List of Recommended tracks given the input information above
    """

    results = sp.recommendations(
        seed_artists=artist_ids,
        seed_genres=genre_ids,
        seed_tracks=track_ids,
        limit=limit,
        country=country,
        **kwargs
    )

    return results

def get_recommendation(track):
    song_list = []
    raw_data = sp.search(q=track, type='track', limit=1)
    track_id = raw_data['tracks']['items'][0]['id']
    recommendation = base_model(track_ids=[track_id])
    for i in range(5):
        song_list.append({"songName": recommendation['tracks'][i]['name'],
                          "artist": recommendation['tracks'][i]['artists'][0]['name'],
                          "song_id": recommendation['tracks'][i]['id']})

    return [song_list]