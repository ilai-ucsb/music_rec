#!/usr/bin/python3

from dotenv import load_dotenv
load_dotenv()

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def base_model(*args, artist_id="0MXwnhyYMeEfij4dl2YIQ4", **kwargs):
    """
    This model gives you the same recommendatio
    """
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    results = spotify.recommendations(
        seed_artists=[artist_id],
        limit=10,
        country='US'
    )

    return results
