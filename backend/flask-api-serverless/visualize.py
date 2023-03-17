import pandas as pd
import plotly.express as px

def visualize_cluster(data, song_embedding):
    """Visualizes the clusters of the song data.

    Args:
        data (dataframe): Pandas dataframe containing song data.
        song_embedding (array): Array containing the PCA embedding of the song data.
    """
    projection = pd.DataFrame(columns=["x", "y"], data=song_embedding)
    projection["title"] = data["name"]
    projection["cluster"] = data["cluster_label"]

    fig = px.scatter(
        projection, x="x", y="y", color="cluster", hover_data=["x", "y", "title"]
    )
    fig.write_image("../../data/cluster.pdf")