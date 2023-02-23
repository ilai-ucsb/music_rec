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

import warnings
warnings.filterwarnings("ignore")



if __name__ == "__main__":
    data = pd.read_csv("data/raw_data.csv")

    # uses 20 clusters, assigns data 
    k_means = KMeans(n_clusters=20, verbose=False, n_jobs=4)
    song_cluster_pipeline = Pipeline([('scalar', StandardScaler()),
                                      ('kmeans', k_means)
                                     ], verbose=False)
    X = data.select_dtypes(np.number)
    number_cols = list(X.columns)
    song_cluster_pipeline.fit(X)
    song_cluster_labels = song_cluster_pipeline.predict(X)
    data['cluster_label'] = song_cluster_labels
