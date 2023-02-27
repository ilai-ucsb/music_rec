import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.metrics import euclidean_distances
from scipy.spatial.distance import cdist
from SpotifyAPICaller import find_song


def k_means_cluster(n_clusters, data):
    """Applies KMeans clustering algorithm to the song data. 
    This clusters songs based the columns with numerical data.

    Args:
        n_clusters (int): Number of clusters to use.
        data (dataframe): Pandas dataframe containing song data.

    Returns:
        data: Pandas dataframe with a new column storing cluster_label 
              based on the KMeans clustering algorithm.
        X (array): Array containing the numerical data of the song data.
    """
    k_means = KMeans(n_clusters=n_clusters, verbose=False, n_jobs=4)
    song_cluster_pipeline = Pipeline([('scalar', StandardScaler()), 
                                      ('kmeans', k_means)
                                     ], verbose=False)
    X = data.select_dtypes(np.number)
    # number_cols = list(X.columns)
    song_cluster_pipeline.fit(X)
    song_cluster_labels = song_cluster_pipeline.predict(X)
    data['cluster_label'] = song_cluster_labels
    return data, X

def visualize_cluster(data, song_embedding):
    """Visualizes the clusters of the song data.

    Args:
        data (dataframe): Pandas dataframe containing song data.
        song_embedding (array): Array containing the PCA embedding of the song data.
    """
    projection = pd.DataFrame(columns=['x', 'y'], data=song_embedding)
    projection['title'] = data['name']
    projection['cluster'] = data['cluster_label']

    fig = px.scatter(
        projection, x='x', y='y', color='cluster', hover_data=['x', 'y', 'title'])
    fig.write_image("../../data/cluster.pdf")

def perform_pca(data, X):
    """Performs PCA on the song data. This reduces the dimensionality of the data.

    Args:
        data (dataframe): Pandas dataframe containing song data.
        X (array): Array containing the numerical data of the song data.

    Returns:
        song_embedding (array): Array containing the PCA embedding of the song data.
    """
    pca_pipeline = Pipeline([('scaler', StandardScaler()), ('PCA', PCA(n_components=2))])
    song_embedding = pca_pipeline.fit_transform(X)
    visualize_cluster(data, song_embedding)
    return song_embedding

def cluster_songs():
    data = pd.read_csv("../../data/raw_data.csv")
    data, X = k_means_cluster(n_clusters=20, data=data)
    song_embedding = perform_pca(data, X)
    
def get_song_data(song, spotify_data):
    """Gets the song data from the dataset or from the Spotify API.

    Args:
        song (_type_): _description_
        spotify_data (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        # find song data from dataset
        song_data = spotify_data[(spotify_data['name'] == song['name'])].iloc[0]
        return song_data
    except IndexError:
        # find song data from spotify API
        return find_song(song['name'])    
    
def get_recommendations(song_name):
    """Gets a recommendation for a song based on the song's cluster.
    
    Args:
        song_name (str): Name of the song to get a recommendation for.
    
    Returns:
        recommendations (list): List of 5 song that are recommended.
    """
    
    return song_name
    

if __name__ == "__main__":
    cluster_songs()
