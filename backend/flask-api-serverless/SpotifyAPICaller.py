from collections import defaultdict
from dotenv import load_dotenv
import logging
import os
import pandas as pd
from random import sample
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import loud
import danceability
import liveness
import energy
import popularity


logging.basicConfig(level=logging.ERROR)

load_dotenv()

client_credentials_manager = SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# code copied from model.py in order to not call spotify oauth multiple times
def base_model(
    artist_ids=None, genre_ids=None, track_ids=None, limit=10, country="US", **kwargs
):
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


def rekofy_model(name, limit, artist):
    """
    Get a list of upto `limit` recommended song using the `Rekofy` model.
    Args:
        name (str) - song name
        limit (int) - The maximum number of recommendations. Default: 100
        artist (str) - artist name (optional)

    Returns:
        List[Song] - A List of Song objects for recommended songs given the input information above
    """
    # This import below is needed to avoid circular dependency import error
    from recommendation import rekofy_get_recommendations

    songs = rekofy_get_recommendations(name, limit, artist)
    return songs


def find_song(name, artist):
    """Find a song given the name using Spotify API

    Args:
        name (str): name of the song to find
        artist (str): name of the artist of the song to find (optional)

    Returns:
        song_data (pd.DataFrame): DataFrame containing the song data or None if not found
    """
    song_data = defaultdict()
    
    # query by artist and track name
    query = name
    if artist != "":
        query += f" artist:{artist}"
    
    # use Spotify API '/search' endpoint to find by track name
    try:
        results = sp.search(q=query, type="track", limit=1)
    except spotipy.SpotifyException as e:
        logging.error(e)
        return None

    if results["tracks"]["items"] == []:
        return None

    results = results["tracks"]["items"][0]
    track_id = results["id"]

    try:
        audio_features = sp.audio_features(track_id)[0]
    except spotipy.SpotifyException as e:
        logging.error(e)
        return None

    song_data["id"] = [track_id]
    song_data["name"] = [results["name"]]
    song_data["year"] = [int(results["album"]["release_date"][:4])]
    song_data["explicit"] = [int(results["explicit"])]
    song_data["duration_ms"] = [results["duration_ms"]]
    song_data["popularity"] = [results["popularity"]]
    song_data["album_cover"] = [results["album"]["images"][0]["url"]]
    song_data["preview_url"] = [results["preview_url"]]

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
    if(type(filters) == dict  and len(filters) > 0):
        good_songs = []
        print("filtering")
        if  "explicit" in filters :
            if filters["explicit"] == "NULL":
                good_songs = song_list
            else :
                for song in song_list:
                    # here we will apply all the filters passed in, but only explicit filters are allowed
                    if bool(filters["explicit"]) == song.explicit:
                        good_songs.append(song)
        else:
            good_songs = song_list
            
        size = 10
        for filter in filters:
            if filters[filter] != "NULL": 
                print(filter)
                print(filters[filter])
                print("good_song pre filter")
                print(good_songs)
                if filter == "loud":
                    good_songs = loud.getLoud(good_songs, filters[filter], size)
                elif filter == "popularity":
                    good_songs = popularity.getPopularity(good_songs, filters[filter], size)
                elif filter == "energy":
                    good_songs = energy.getEnergy(good_songs, filters[filter], size)
                elif filter == "liveness":
                    good_songs = liveness.getLiveness(good_songs, filters[filter], size)
                elif filter == "danceability":
                    good_songs = danceability.getDanceability(good_songs, filters[filter], size)
                # elif filter == "minYear":
                #     good_songs = year.getYear(good_songs, filters["minYear"], filters["maxYear"], size)
                print("good_song after filter")
                print(good_songs)

            size -= 1
        if(len(good_songs) < 5):
            return good_songs
        else:
            return good_songs[0:5]
    else : 
        return song_list
    

def get_recommendation(track, filters, artist):
    song_list = []
    song_recommendations = rekofy_model(name=track, limit=10, artist=artist)
    print("get rec")
    filtered_recommendations = filter_songs(song_recommendations, filters)
    #print(filtered_recommendations[0])
    print(song_recommendations)
    print("rec filtered")
    if len(filtered_recommendations) > 5:
        filtered_recommendations = sample(filtered_recommendations, 5)
        
    for s in filtered_recommendations:
        song_list.append(
            {
                "songName": s.name,
                "artist": s.artists.split("'")[1],
                "song_id": s.id,
                "explicit": str(s.explicit),
                "popularity": s.popularity,
                "year": s.year,
                "danceability": str(s.danceability)[0:5],
                "acousticness": str(s.acousticness)[0:5],
                "energy": str(s.energy)[0:5],
                "instrumentalness": str(s.instrumentalness)[0:5],
                "liveness": str(s.liveness),
                "loudness": str(s.loudness)[0:5],
                "speechiness": str(s.speechiness),
                "tempo": str(s.tempo),
                "album_cover": s.album_cover,
                "preview_url": s.preview_url,
            }
        )
    return [song_list]
