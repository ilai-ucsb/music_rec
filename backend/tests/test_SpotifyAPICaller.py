import numpy as np
import pandas as pd

from backend_imports import app, SpotifyAPICaller as caller, song, limits

# Popular Songs for testing
GANGNAM_STYLE = "Gangnam Style"
DESPACITO = "Despacito"
INVALID_SONG = "nbdjs183hdjhkzxiuoq2uqejhsjhks"


def test_get_recommendations_no_filters():
    response = app.test_client().post("/result", json={"name": GANGNAM_STYLE})
    assert (
        response.get_json() != None and len(response.get_json()["name"][0]) <= 5
    ), f"Unknown error occurred for response: {response}"


def test_get_recommendations_null_explicit():
    response = app.test_client().post(
        "/result", json={"name": "gangnam style", "filters": {"explicit": "NULL"}}
    )
    assert (
        response.get_json() != None and len(response.get_json()["name"][0]) <= 5
    ), f"Unknown error occurred for response: {response}"


def test_get_recommendations_0_explicit():
    response = app.test_client().post(
        "/result", json={"name": "gangnam style", "filters": {"explicit": 0}}
    )
    df = pd.DataFrame(response.get_json()["name"][0])

    assert response.status_code == 200, f"Bad response code {response.status_code}"

    assert (
        response.get_json() != None and len(response.get_json()["name"][0]) <= 5
    ), f"Unknown error occurred for response: {response}"
    assert (df["explicit"] == False).sum() == len(
        df
    ), f"explicit filter did not work! {response.get_json()}"


def test_get_recommendations_1_explicit():
    response = app.test_client().post(
        "/result", json={"name": GANGNAM_STYLE, "filters": {"explicit": 1}}
    )
    df = pd.DataFrame(response.get_json()["name"][0])
    assert (
        response.get_json() != None and len(response.get_json()["name"][0]) <= 5
    ), f"Unknown error occurred for response: {response.get_json()}"
    assert (df["explicit"] == True).sum() == len(
        df
    ), f"explicit filter did not work! {response.get_json()}"


def test_find_song_gangnam_style():
    song_df = caller.find_song(GANGNAM_STYLE)
    assert (
        not song_df.empty and not song_df.columns.empty
    ), f"Could not find song: {GANGNAM_STYLE}"
    assert set(song.Song.SPOTIFY_API_GOLDEN_COLUMNS).issubset(
        set(song_df.columns)
    ), f"Could not find song: {GANGNAM_STYLE}"
    assert (
        isinstance(song_df["name"][0], str)
        and GANGNAM_STYLE in song_df["name"][0]
    ), f"Song name is not a valid string: {song_df['name'][0]}"
    assert isinstance(
        song_df["id"][0], str
    ), f"Song id is not a valid string: {song_df['id'][0]}"
    assert isinstance(
        song_df["year"][0], np.integer
    ), f"Song year is not a valid int: {song_df['year'][0]}"
    assert isinstance(
        song_df["explicit"][0], np.integer
    ), f"Song explicit is not a valid int: {song_df['explicit'][0]}"
    assert isinstance(
        song_df["duration_ms"][0], np.integer
    ), f"Song duration_ms is not a valid int: {song_df['duration_ms'][0]}"
    assert isinstance(
        song_df["popularity"][0], np.integer
    ), f"Song popularity is not a valid int: {song_df['popularity'][0]}"
    assert isinstance(
        song_df["album_cover"][0], str
    ), f"Song album_cover is not a valid string: {song_df['album_cover'][0]}"


def test_find_song_despacito():
    song_df = caller.find_song(DESPACITO)
    assert (
        not song_df.empty and not song_df.columns.empty
    ), f"Could not find song: {DESPACITO}"
    assert set(song.Song.SPOTIFY_API_GOLDEN_COLUMNS).issubset(
        set(song_df.columns)
    ), f"Could not find song: {DESPACITO}"
    assert (
        isinstance(song_df["name"][0], str)
        and DESPACITO in song_df["name"][0]
    ), f"Song name is not a valid string: {song_df['name'][0]}"
    assert isinstance(
        song_df["id"][0], str
    ), f"Song id is not a valid string: {song_df['id'][0]}"
    assert isinstance(
        song_df["year"][0], np.integer
    ), f"Song year is not a valid int: {song_df['year'][0]}"
    assert isinstance(
        song_df["explicit"][0], np.integer
    ), f"Song explicit is not a valid int: {song_df['explicit'][0]}"
    assert isinstance(
        song_df["duration_ms"][0], np.integer
    ), f"Song duration_ms is not a valid int: {song_df['duration_ms'][0]}"
    assert isinstance(
        song_df["popularity"][0], np.integer
    ), f"Song popularity is not a valid int: {song_df['popularity'][0]}"
    assert isinstance(
        song_df["album_cover"][0], str
    ), f"Song album_cover is not a valid string: {song_df['album_cover'][0]}"


def test_find_song_invalid():
    song_df = caller.find_song(INVALID_SONG)
    assert song_df == None, f"Unknown error occurred for song: {INVALID_SONG}"


def test_find_song_null():
    song_df = caller.find_song(None)
    assert song_df == None, f"Unknown error occurred for song: {song_df}"

def test_similar_failing():
    response = app.test_client().post("/similar", json="")
    assert response.status_code == 500, "Expected a failing status code here, not 500"

def test_similar_bad_arg():
    params = {
        "n": 5,
        "loudness": 0.5,
        "min_year": 2016,  # this fails because min year is not a valid filter name
    }
    response = app.test_client().post("/similar", json=params)

    assert response.status_code == 500, f"Expected failing because min_year is not expected to be passing"

def test_similar_passing():
    params = {
        "n": 5,
        "loudness": 0.5,
        "year": 2016
    }
    response = app.test_client().post("/similar", json=params)

    assert response.status_code == 200, f"Expected passing status code, not {response.status_code}"

    data = response.get_json()["similar_songs"]

    assert len(data) <= params["n"], f"Expected less than or equal to {params['n']} songs returned"
    
    # params.pop("n", None)
    # params.pop("threshold", None)

    # yr_minimum = limits.VALIDATION_TABLE["year"]["minimum"]
    # yr_maximum = limits.VALIDATION_TABLE["year"]["maximum"]

    # for fltr, val in params.items():
    #     factor = limits.VALIDATION_TABLE[fltr]["maximum"] - limits.VALIDATION_TABLE[fltr]["minimum"]
    #     for row in data:
    #         assert abs(row[fltr] - val) <= 0.05 * factor, f"Filter {fltr} was not within threshold"  # 0.05 is the default threshold

if __name__ == "__main__":
    test_similar_bad_arg()
