from tqdm import tqdm
import pandas as pd
import song
import config
import logging

def _configure_api():
    """
    Configures Spotify API using python Spotipy

    Returns: Configured Spotify client
    """
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    from dotenv import load_dotenv, find_dotenv
    import os

    load_dotenv(find_dotenv())

    client_credentials_manager = SpotifyClientCredentials(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'))

    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    return sp

def get_spotify_api_data(id):
    """
    Given song id, returns Spotify API song data features:
    - popularity
    - artists
    - artist popularity
    - genres
    - danceability
    - acousticness
    - energy
    - instrumentalness
    - liveness
    - loudness
    - speechiness
    - tempo
    """
    track_uri = "spotify:track:" + id
    sp = _configure_api()
    track = sp.track(track_uri)
    _pop = track["popularity"]
    _artists = [track["artists"][i]["name"] for i in range(len(track["artists"]))]

    # artist info
    artist_uri = track["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    _artist_pop =  artist_info["popularity"]
    _genres = artist_info["genres"]

    # audio features
    track_uri = track["uri"]
    audio_f = sp.audio_features(track_uri)[0]
    _danceability = audio_f["danceability"]
    _acousticness = audio_f["acousticness"]
    _energy = audio_f["energy"]
    _instrumentalness = audio_f["instrumentalness"]
    _liveness = audio_f["liveness"]
    _loudness = audio_f["loudness"]
    _speechiness = audio_f["speechiness"]
    _tempo = audio_f["tempo"]

    return (_pop, _artists, _artist_pop, _genres, _danceability, 
    _acousticness, _energy, _instrumentalness, _liveness, 
    _loudness, _speechiness, _tempo)

def _setup_database():
    """
    Configures the Cloud Firestore Database by adding credentials to
    authenticate user.
    """
    import firebase_admin
    from firebase_admin import credentials
    import os

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.DATABASE_CERT
    cred = credentials.Certificate(config.DATABASE_CERT)
    firebase_admin.initialize_app(cred)

def add_song(key, song_dict):
    """
    Adds a `new` song to 'Song' collection in the Firestore
    database given the key and song_dict

    Input:
        key: Spotify song id (database key)
        song_dict: python dictionary of song features pushed
                   as the value of the database document
    """
    from firebase_admin import firestore

    db = firestore.client()
    song_collection = db.collection(u'Songs')
    doc = song_collection.document(key)
    if doc.get().to_dict() != None:
        raise ValueError("Adding an existing song to the database. You must update an existing song entry.")
    doc.set(song_dict)

def update_song(key, song_dict):
    """
    Updates an existing song to 'Song' collection in the
    Firestore database given the key and song_dict

    Input:
        key: Spotify song id (database key)
        song_dict: python dictionary of song features pushed
                   as the value of the database document
    """
    from firebase_admin import firestore
    
    db = firestore.client()
    song_collection = db.collection('Songs')
    song_collection.document(key).set(song_dict)


def _process(data):
    """
    This method takes in path to dataset.

    For each song in dataset:
    - Get raw data from CSV
    - Get values from Spotipy API
    - Save info as song
    - Add song to Firestore database
    """

    # read pandas dataframe
    df = pd.read_csv(data)

    # There are 170653 total songs. 133638 songs with unique names,
    # so we should store songs by id.
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Total No. of songs {df.shape[0]}")
    logging.info(f"No. songs with unique names {len(pd.unique(df['name']))}")
    logging.info(f"No. songs with unique ids {len(pd.unique(df['id']))}")

    for i in tqdm(range(df.shape[0])):
        item = df.loc[i]

        # get data from csv
        _id = item.at["id"]
        _name = item.at["name"]
        _year = item.at["year"]
        _explicit = item.at["explicit"]

        # get value from api 
        (_pop, _artists, _artist_pop, _genres, _danceability, 
        _acousticness, _energy, _instrumentalness, 
        _liveness, _loudness, _speechiness, _tempo)  = get_spotify_api_data(_id)

        # add song dict to database
        add_song(_id, song.Song(_id, _name, _pop, _year, _artists, _artist_pop,
        _genres, _danceability, _acousticness, _energy, _explicit,
        _instrumentalness, _liveness, _loudness, _speechiness, _tempo).to_dict())


if __name__ == "__main__":
    _setup_database()
    _process(config.DATA_DIR)
