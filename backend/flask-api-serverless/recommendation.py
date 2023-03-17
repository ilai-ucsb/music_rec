import numpy as np
import pandas as pd
import pickle as pkl
import os
import sys

from collections import defaultdict
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from SpotifyAPICaller import find_song

sys.path.append("..")
from database import song

Song = song.Song


song_cluster_pipeline = None
data = None


def k_means_cluster(n_clusters, data):
    """Applies KMeans clustering algorithm to the song data.
    This clusters songs based the columns with numerical data.

    Args:
        n_clusters (int): Number of clusters to use.
        data (dataframe): Pandas dataframe containing song data.

    Returns:
        song_cluster_pipeline (Pipeline): Pipeline containing the KMeans clustering algorithm.
        data: Pandas dataframe with a new column storing cluster_label
              based on the KMeans clustering algorithm.
        X (array): Array containing the numerical data of the song data.
    """
    k_means = KMeans(n_clusters=n_clusters, verbose=False)

    song_cluster_pipeline = Pipeline(
        [("scalar", StandardScaler()), ("kmeans", k_means)], verbose=False
    )
    X = data.select_dtypes(np.number)
    song_cluster_pipeline.fit(X)
    song_cluster_labels = song_cluster_pipeline.predict(X)
    data["cluster_label"] = song_cluster_labels

    with open("rekofy.pkl", "wb") as f:
        pkl.dump(song_cluster_pipeline, f)  # serialize the list

    return song_cluster_pipeline, data, X

def perform_pca(data, X):
    """Performs PCA on the song data. This reduces the dimensionality of the data.

    Args:
        data (dataframe): Pandas dataframe containing song data.
        X (array): Array containing the numerical data of the song data.

    Returns:
        song_embedding (array): Array containing the PCA embedding of the song data.
    """
    pca_pipeline = Pipeline(
        [("scaler", StandardScaler()), ("PCA", PCA(n_components=2))]
    )
    song_embedding = pca_pipeline.fit_transform(X)
    return song_embedding


def cluster_songs():
    global song_cluster_pipeline, data
    data = pd.read_csv("../../data/raw_data.csv")
    song_cluster_pipeline, data, X = k_means_cluster(n_clusters=20, data=data)
    song_embedding = perform_pca(data, X)


def get_song_data(song, spotify_data, artist):
    """Gets the song data from the dataset or from the Spotify API.

    Args:
        song (str): song name string
        spotify_data (pd.DataFrame): DataFrame containing entire song dataset
        artist (str): artist name string

    Returns:
        song_data (pd.DataFrame): DataFrame containing the song data
    """
    try:
        # find song data from dataset
        song_data = spotify_data[(spotify_data["name"] == song["name"])].iloc[0]
        return song_data
    except IndexError:
        # find song data from spotify API with artist name
        return find_song(song["name"], artist)


number_cols = [
    "valence",
    "year",
    "acousticness",
    "danceability",
    "duration_ms",
    "energy",
    "explicit",
    "instrumentalness",
    "key",
    "liveness",
    "loudness",
    "mode",
    "popularity",
    "speechiness",
    "tempo",
]


def get_mean_vector(song_list, spotify_data, artist):
    song_vectors = []

    for song in song_list:
        song_data = get_song_data(song, spotify_data, artist)
        if song_data is None:
            continue
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector)

    song_matrix = np.array(list(song_vectors))
    return np.mean(song_matrix, axis=0)


def flatten_dict_list(dict_list):
    flattened_dict = defaultdict()
    for key in dict_list[0].keys():
        flattened_dict[key] = []

    for dict_ in dict_list:
        for key, value in dict_.items():
            flattened_dict[key].append(value)

    return flattened_dict


def recommend_songs(song_list, spotify_data, artist, n_songs=10):
    global song_cluster_pipeline

    with open(os.path.dirname(__file__) + "/rekofy.pkl", "rb") as f:
        song_cluster_pipeline = pkl.load(f)

    metadata_cols = ["name", "year", "artists"]
    song_dict = flatten_dict_list(song_list)

    song_center = get_mean_vector(song_list, spotify_data, artist)
    scalar = song_cluster_pipeline.steps[0][1]
    scaled_data = scalar.transform(spotify_data[number_cols])
    scaled_song_center = scalar.transform(song_center.reshape(1, -1))
    distances = cdist(scaled_song_center, scaled_data, "cosine")
    index = list(np.argsort(distances)[:, :n_songs][0])

    rec_songs = spotify_data.iloc[index]
    rec_songs = rec_songs[~rec_songs["name"].isin(song_dict["name"])]
    return rec_songs.to_dict("records")


def rekofy_get_recommendations(song_names, num_songs=5, artist=""):
    """Gets a recommendation for a song based on the song's cluster.

    Args:
        song_names (list): List of song names to get a recommendation for.
        num_songs (int): Number of songs to recommend.
        artist (str): Artist name of the song. (optional)

    Returns:
        recommendations (list): List of 5 song that are recommended.
    """
    global data
    input_dict_list = []
    recommendations = []
    data = pd.read_csv("../../data/raw_data.csv")

    input_dict_list.append({"name": song_names})
    output_dict = recommend_songs(input_dict_list, data, artist, n_songs=num_songs)

    for song in output_dict:
        _song = Song.from_dict(song)
        song_df = find_song(_song.name, "")
        if song_df is None:
            continue
        _song.album_cover = song_df["album_cover"][0]
        _song.preview_url = song_df["preview_url"][0]
        _song.explicit = song_df["explicit"][0]

        recommendations.append(_song)

    return recommendations
