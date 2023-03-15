import numpy as np
import pandas as pd
import pickle as pkl
# import seaborn as sns
import plotly.express as px
# import matplotlib.pyplot as plt
import sys

from collections import defaultdict
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from SpotifyAPICaller import find_song
# from sklearn.manifold import TSNE
# from sklearn.metrics import euclidean_distances
# import joblib

sys.path.append('..')
from database.song import Song

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

    song_cluster_pipeline = Pipeline([('scalar', StandardScaler()), 
                                      ('kmeans', k_means)
                                     ], verbose=False)
    X = data.select_dtypes(np.number)
    # number_cols = list(X.columns)
    song_cluster_pipeline.fit(X)
    song_cluster_labels = song_cluster_pipeline.predict(X)
    data['cluster_label'] = song_cluster_labels
    
    # joblib.dump(song_cluster_pipeline, 'song.pkl', compress = 1)
    with open('song.pkl', 'wb') as f:
        pkl.dump(song_cluster_pipeline, f) # serialize the list
    
    return song_cluster_pipeline, data, X

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
    global song_cluster_pipeline, data
    data = pd.read_csv("../../data/raw_data.csv")
    song_cluster_pipeline, data, X = k_means_cluster(n_clusters=20, data=data)
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
        return findx_song(song['name'])   

number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']
 
def get_mean_vector(song_list, spotify_data):
    song_vectors = []
    
    for song in song_list:
        song_data = get_song_data(song, spotify_data)
        if song_data is None:
            print('Error: {} does not exist in Spotify or in database'.format(song['name']))
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

def recommend_songs(song_list, spotify_data, n_songs=10):
    global song_cluster_pipeline
    # if song_cluster_pipeline is None:
    #     cluster_songs()
    # spotify_data = pd.read_csv("../../data/raw_data.csv")

    print("loading file")
    with open('song.pkl', 'rb') as f:
        song_cluster_pipeline = pkl.load(f)
        # pkl.dump(song, f) # serialize the list
    
    print("done loading model")

    metadata_cols = ['name', 'year', 'artists']
    song_dict = flatten_dict_list(song_list)
    
    song_center = get_mean_vector(song_list, spotify_data)
    scalar = song_cluster_pipeline.steps[0][1]
    scaled_data = scalar.transform(spotify_data[number_cols])
    scaled_song_center = scalar.transform(song_center.reshape(1, -1))
    distances = cdist(scaled_song_center, scaled_data, 'cosine')
    index = list(np.argsort(distances)[:, :n_songs][0])
    
    rec_songs = spotify_data.iloc[index]
    rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]  
    
    return rec_songs.to_dict('records')
    # return Song.from_dict(rec_songs.to_dict('records'))
    # return rec_songs[metadata_cols].to_dict('records')

def rekofy_get_recommendations(song_names, num_songs=5):
    """Gets a recommendation for a song based on the song's cluster.
    
    Args:
        song_names (list): List of song names to get a recommendation for.
    
    Returns:
        recommendations (list): List of 5 song that are recommended.
    """
    global data
    input_dict_list = []
    recommendations = []
    data = pd.read_csv("../../data/raw_data.csv")
        
    for song in song_names:
        dict_ = {'name': song}
        input_dict_list.append(dict_)
    
    output_dict = recommend_songs(input_dict_list, data, n_songs=num_songs)
    print(len(output_dict))
    
    for song in output_dict:
        _song = Song.from_dict(song)
        # print(find_song(_song.name)['album_cover'][0])
        song_df = find_song(_song.name)
        _song.album_cover = song_df['album_cover'][0]
        _song.preview_url = song_df['preview_url'][0]
        _song.explicit = song_df['explicit'][0]
        
        recommendations.append(_song)
    
    return recommendations
    

if __name__ == "__main__":
    # cluster_songs()
    # songs = get_recommendations(['Shape of You', 'Despacito'], 50)
    songs = rekofy_get_recommendations(['Gangnam Style'], 100)
    for s in songs:
        if s.explicit == 1:
            print(s.name)
    # print(get_recommendations(['As it was']))
    # q: What are the Top Hit songs of this decade?
    # a: ['Shape of You', 'Despacito', 'One Dance', 'Closer', 'Rockstar', 'Havana', 'I Like It', 'Dance Monkey', 'Senorita', 'Sunflower']
