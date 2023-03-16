import logging
from collections import defaultdict
import os
import pandas as pd
import spotipy
import random

from collections import defaultdict
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials
from random import sample

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

def rekofy_model(name, limit):
    from recommendation import rekofy_get_recommendations
    songs = rekofy_get_recommendations(name, limit)
    return songs

def find_song(name):
    """Find a song given the name using Spotify API
    
    Args:
        name (str): name of the song to find
        
    Returns:
        song_data (pd.DataFrame): DataFrame containing the song data or None if not found
    """
    song_data = defaultdict()
    
    # use Spotify API '/search' endpoint to find by track name
    try:
        results = sp.search(q=name, type='track', limit=1)
    except spotipy.SpotifyException as e:
        logging.error(e)
        return None
    
    if results['tracks']['items'] == []:
        return None
    
    results = results['tracks']['items'][0]
    track_id = results['id']
    
    
    try:
        audio_features = sp.audio_features(track_id)[0]
    except spotipy.SpotifyException as e:
        logging.error(e)
        return None
    
    # print(results)
    
    song_data['id'] = [track_id]
    song_data['name'] = [results['name']]
    song_data['year'] = [int(results['album']['release_date'][:4])]
    song_data['explicit'] = [int(results['explicit'])]
    song_data['duration_ms'] = [results['duration_ms']]
    song_data['popularity'] = [results['popularity']]
    song_data['album_cover'] = [results['album']['images'][0]['url']]
    song_data['preview_url'] = [results['preview_url']]
    
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
    print("IN FILTER SONGS:")
    print(song_list)
    for song in song_list:
        # here we will apply all the filters passed in, but only explicit filters are allowed
        # if filters.get("explicit", None) and bool(filters["explicit"]) == song["explicit"]:
        print(song.explicit)
        if filters.get("explicit", None) and int(filters["explicit"]) == song.explicit:
            good_songs.append(song)
        elif filters.get("explicit", None) == None:
            good_songs.append(song)
    print(good_songs)
    return good_songs

def get_recommendation(track, filters):
    """

    Args:
        track (str): Name of the song.
        filters (): 

    Returns:
        _type_: _description_
    """
    song_list = []
    # raw_data = sp.search(q=track, type='track', limit=1)
    # try:
        # track_id = raw_data['tracks']['items'][0]['id']
    # except LookupError as lerr:  # covers index error and key error
        # logging.error("Could not retrieve the track id for the song passed in.")
        # raise  # bad input track
    
    # base model
    # recommendation = base_model(track_ids=[track_id], limit=30)

    # rekofy model
    song_recommendations = rekofy_model(name=track, limit=100)
    # song_recommendations = sample(song_recommendations, 5)
    # print(song_recommendations)
    
    for s in song_recommendations:
        print(s.to_dict())
    
    # song_recommendations = random.shuffle(song_recommendations)
    # filtered_recommendations = song_recommendations
    # filter_songs(song_recommendations, filters)
    # for song in filtered_recommendations[:5]:
    #     song_list.append({"songName": song['name'],
    #                       "artist": song['artists'][0]['name'],
    #                       "song_id": song['id'],
    #                       "explicit": song["explicit"]})

    filtered_recommendations = filter_songs(song_recommendations, filters)
    print(filtered_recommendations)
    if len(filtered_recommendations) > 5:
        filtered_recommendations = sample(filtered_recommendations, 5)
    print(filtered_recommendations)
    for s in filtered_recommendations:
        song_list.append({
            "songName": s.name,
            "artist": s.artists.split("'")[1],
            "song_id": s.id,
            "explicit": str(s.explicit),
            "popularity": s.popularity,
            "year": s.year,
            "danceability": str(s.danceability)[0:5],
            "acousticness": str(s.acousticness)[0:5],
            "energy": str(s.energy),
            "instrumentalness": str(s.instrumentalness)[0:5],
            "liveness": str(s.liveness),
            "loudness": str(s.loudness)[0:5],
            "speechiness": str(s.speechiness),
            "tempo": str(s.tempo),
            "album_cover": s.album_cover,
            "preview_url": s.preview_url
        })
    return [song_list]
    
    
    # FIX THIS PART OF THE CODE LATER :(
    # filtered_recommendations = filter_songs(recommendation["tracks"], filters)
    # for song in filtered_recommendations[:5]:
    #     song_list.append({"songName": song['name'],
    #                       "artist": song['artists'][0]['name'],
    #                       "song_id": song['id'],
    #                       "explicit": song["explicit"]})

    # return [song_list]

if __name__ == "__main__":
    songs = rekofy_model("Gangnam Style", 100)
    for s in songs:
        if s.explicit == 0:
            print(s.name)      
        # print(s.artists)
        # arr = s.artists.split("'")
        # print(arr[0])
        # print(s.artists.split("'")[1])
        # print(s.id)
        # print(s.explicit)