import sys
sys.path.append('..')

import pandas as pd

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

def test_find_song_gangnam():
    df = find_song(Song.GANGNAM_STYLE)
    assert not df.empty and not df.columns.empty, f"Could not find song: {Song.GANGNAM_STYLE}"
    assert set(Song.SPOTIFY_API_GOLDEN_COLUMNS).issubset(df), f"Could not find song: {Song.GANGNAM_STYLE}"
    assert isinstance(df['name'][0], str) and Song.GANGNAM_STYLE in df['name'][0], f"Song name not valid string: {df['name'][0]}"

def test_find_song_despacito():
    df = find_song(Song.DESPACITO)
    assert not df.empty and not df.columns.empty, f"Could not find song: {Song.DESPACITO}"
    assert set(Song.SPOTIFY_API_GOLDEN_COLUMNS).issubset(df), f"Could not find song: {Song.DESPACITO}"
    assert isinstance(df['name'][0], str) and Song.DESPACITO in df['name'][0], f"Song name not valid string: {df['name'][0]}"
  
def test_find_song_invalid():
    df = find_song(Song.INVALID_SONG)
    assert df == None, f"Could not find song: {Song.INVALID_SONG}"