import numpy as np
import pandas as pd
import sys
sys.path.append('..')

from app import app
from SpotifyAPICaller import find_song
sys.path.append('../..')
from database.song import Song

def test_get_recommendations_no_filters():
    response = app.test_client().post("/result", json={"name": Song.GANGNAM_STYLE})
    assert response.get_json() != None and len(response.get_json()['name'][0]) <= 5, f"Unknown error occurred for response: {response}"

def test_get_recommendations_null_explicit():
    response = app.test_client().post("/result", json={"name": Song.GANGNAM_STYLE, "filters": {"explicit": "NULL"}})
    assert response.get_json() != None and len(response.get_json()['name'][0]) <= 5, f"Unknown error occurred for response: {response}"

def test_get_recommendations_0_explicit():
    response = app.test_client().post("/result", json={"name": Song.GANGNAM_STYLE, "filters": {"explicit": 0}})
    print(response.get_json())
    df = pd.DataFrame(response.get_json()["name"][0])
    assert response.get_json() != None and len(response.get_json()['name'][0]) <= 5, f"Unknown error occurred for response: {response}"
    assert (df["explicit"] == False).sum() == len(df), f"explicit filter did not work! {response.get_json()}"

def test_get_recommendations_1_explicit():
    response = app.test_client().post("/result", json={"name": Song.GANGNAM_STYLE, "filters": {"explicit": 1}})
    df = pd.DataFrame(response.get_json()["name"][0])
    assert response.get_json() != None and len(response.get_json()['name'][0]) <= 5, f"Unknown error occurred for response: {response.get_json()}"
    assert (df["explicit"] == True).sum() == len(df), f"explicit filter did not work! {response.get_json()}"

def test_find_song_gangnam_style():
    song_df = find_song(Song.GANGNAM_STYLE)
    assert not song_df.empty and not song_df.columns.empty, f"Could not find song: {Song.GANGNAM_STYLE}"
    assert set(Song.SPOTIFY_API_GOLDEN_COLUMNS).issubset(set(song_df.columns)), f"Could not find song: {Song.GANGNAM_STYLE}"
    assert isinstance(song_df['name'][0], str) and Song.GANGNAM_STYLE in song_df['name'][0], f"Song name is not a valid string: {song_df['name'][0]}"
    assert isinstance(song_df['id'][0], str), f"Song id is not a valid string: {song_df['id'][0]}"
    assert isinstance(song_df['year'][0], np.integer), f"Song year is not a valid int: {song_df['year'][0]}"
    assert isinstance(song_df['explicit'][0], np.integer), f"Song explicit is not a valid int: {song_df['explicit'][0]}"
    assert isinstance(song_df['duration_ms'][0], np.integer), f"Song duration_ms is not a valid int: {song_df['duration_ms'][0]}"
    assert isinstance(song_df['popularity'][0], np.integer), f"Song popularity is not a valid int: {song_df['popularity'][0]}"
    
def test_find_song_despacito():
    song_df = find_song(Song.DESPACITO)
    assert not song_df.empty and not song_df.columns.empty, f"Could not find song: {Song.DESPACITO}"
    assert set(Song.SPOTIFY_API_GOLDEN_COLUMNS).issubset(set(song_df.columns)), f"Could not find song: {Song.DESPACITO}"
    assert isinstance(song_df['name'][0], str) and Song.DESPACITO in song_df['name'][0], f"Song name is not a valid string: {song_df['name'][0]}"
    assert isinstance(song_df['id'][0], str), f"Song id is not a valid string: {song_df['id'][0]}"
    assert isinstance(song_df['year'][0], np.integer), f"Song year is not a valid int: {song_df['year'][0]}"
    assert isinstance(song_df['explicit'][0], np.integer), f"Song explicit is not a valid int: {song_df['explicit'][0]}"
    assert isinstance(song_df['duration_ms'][0], np.integer), f"Song duration_ms is not a valid int: {song_df['duration_ms'][0]}"
    assert isinstance(song_df['popularity'][0], np.integer), f"Song popularity is not a valid int: {song_df['popularity'][0]}"
    
def test_find_song_invalid():
    song_df = find_song(Song.INVALID_SONG)
    assert song_df == None, f"Unknown error occurred for song: {Song.INVALID_SONG}"

def test_find_song_null():
    song_df = find_song(None)
    assert song_df == None, f"Unknown error occurred for song: {None}"