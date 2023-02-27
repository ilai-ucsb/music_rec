import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import pandas as pd
import logging
from collections import defaultdict

logging.basicConfig(level=logging.ERROR)

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

def find_song(name):
    """Find a song by name
    
    Args:
        name (str): name of the song to find
        
    Returns:
        song_data (pd.DataFrame): dataframe containing the song data
    """
    song_data = defaultdict()
    results = sp.search(q=name, type='track', limit=1)
    
    if results['tracks']['items'] == []:
        return None
    
    results = results['tracks']['items'][0]
    track_id = results['id']
    audio_features = sp.audio_features(track_id)[0]
    
    song_data['id'] = [track_id]
    song_data['name'] = [name]
    song_data['year'] = [int(results['album']['release_date'][:4])]
    song_data['explicit'] = [int(results['explicit'])]
    song_data['duration_ms'] = [results['duration_ms']]
    song_data['popularity'] = [results['popularity']]
    
    for key, value in audio_features.items():
        song_data[key] = [value]
    return pd.DataFrame(song_data)

def filter_songs(song_list, filters):
    """Process the filters over the song list and return filtered songs

    Args:
        song_list (list): list of songs to filter
        filters (dict): filters to apply to the song list

    Returns:
        (list): filtered songs
    """
    if type(filters) == dict and filters.get("explicit", "NULL") == "NULL":  # remove NULL explicit filter
        filters.pop("explicit", None)
    if filters == None or len(filters) == 0:
        return song_list
    good_songs = []
    for song in song_list:
        # here we will apply all the filters passed in, but only explicit filters are allowed
        if bool(filters["explicit"]) == song["explicit"]:
            good_songs.append(song)
    return good_songs

def get_recommendation(track, filters):
    song_list = []
    raw_data = sp.search(q=track, type='track', limit=1)
    try:
        track_id = raw_data['tracks']['items'][0]['id']
    except LookupError as lerr:  # covers index error and key error
        logging.error("Could not retrieve the track id for the song passed in.")
        raise  # bad input track
    recommendation = base_model(track_ids=[track_id], limit=30)
    filtered_recommendations = filter_songs(recommendation["tracks"], filters)
    for song in filtered_recommendations[:5]:
        song_list.append({"songName": song['name'],
                          "artist": song['artists'][0]['name'],
                          "song_id": song['id'],
                          "explicit": song["explicit"]})

    return [song_list]
