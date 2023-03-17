class Song(object):
    # SPOTIFY_API_GOLDEN_COLUMNS: set columns
    SPOTIFY_API_GOLDEN_COLUMNS = (
        "id",
        "name",
        "year",
        "explicit",
        "duration_ms",
        "popularity",
        "danceability",
        "instrumentalness",
        "energy",
        "mode",
        "speechiness",
        "acousticness",
        "tempo",
        "key",
        "loudness",
        "valence",
        "liveness",
        "time_signature",
    )
    """
    The Song object contains all features for each song.

    Arguments:
        - id, (spotify track id)
        - name (string: track name)
        - popularity (double: track popularity)
        - year (integer: track release year)
        - artists (string: track artist name)
        - danceability (double: between 0 and 1)
        - acouticness (double: between 0 and 1)
        - energy (double: between 0 and 1)
        - explicit (boolean: either 0 or 1)
        - instrumentalness (double: between 0 and 1)
        - liveness (double)
        - loudness (double)
        - speechiness (double)
        - tempo (double)
        - album_cover (string: album cover link)
        - preview_url (string: 30 second preview link)
        - artist_pop (double: track artist popularity)
        - artist_genres (string[]: track artist genres)
    """

    def __init__(
        self,
        id,
        name,
        popularity,
        year,
        artists,
        danceability,
        acousticness,
        energy,
        explicit,
        instrumentalness,
        liveness,
        loudness,
        speechiness,
        tempo,
        album_cover="",
        preview_url="",
        artist_pop=0,
        genres=[],
    ):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.year = year
        self.artists = artists
        self.artist_pop = artist_pop
        self.genres = genres
        self.danceability = danceability
        self.acousticness = acousticness
        self.energy = energy
        self.explicit = explicit
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.loudness = loudness
        self.speechiness = speechiness
        self.tempo = tempo
        self.album_cover = album_cover
        self.preview_url = preview_url

    @staticmethod
    def from_dict(source):
        song = Song(
            source["id"],
            source["name"],
            source["popularity"],
            source["year"],
            source["artists"],
            source["danceability"],
            source["acousticness"],
            source["energy"],
            source["explicit"],
            source["instrumentalness"],
            source["liveness"],
            source["loudness"],
            source["speechiness"],
            source["tempo"],
        )
        if "genres" in source:
            song.genres = source["genres"]
        if "artist_pop" in source:
            song.artist_pop = source["artist_pop"]
        if "album_cover" in source:
            song.album_cover = source["album_cover"]
        if "preview_url" in source:
            song.preview_url = source["preview_url"]
        return song

    def to_dict(self):
        dest = {
            "id": self.id,
            "name": self.name,
            "popularity": self.popularity,
            "artists": self.artists,
            "artists_pop": self.artist_pop,
            "danceability": self.danceability,
            "acousticness": self.acousticness,
            "energy": self.energy,
            "explicit": self.explicit,
            "instrumentalness": self.instrumentalness,
            "liveness": self.liveness,
            "loudness": self.loudness,
            "speechiness": self.speechiness,
            "tempo": self.tempo,
            "album_cover": self.album_cover,
            "preview_url": self.preview_url,
        }

        if self.year:
            # dest[u'year'] = self.year.item()
            dest["year"] = self.year

        if self.genres:
            dest["genres"] = self.genres

        return dest

    def __repr__(self):
        return (
            f"Song(id={self.id}, "
            + f"name={self.name}, "
            + f"popularity={self.popularity}, "
            + f"year={self.year}, "
            + f"artists={self.artists}, "
            + f"artist_pop={self.artist_pop}, "
            + f"genres={self.genres}, "
            + f"danceability={self.danceability}, "
            + f"acousticness={self.acousticness}, "
            + f"energy={self.energy}, "
            + f"explicit={self.explicit}, "
            + f"instrumentalness={self.instrumentalness}, "
            + f"liveness={self.liveness}, "
            + f"loudness={self.loudness}, "
            + f"speechiness={self.speechiness}, "
            + f"tempo={self.tempo}, "
            + f"album_cover={self.album_cover}, "
            + f"preview_url={self.preview_url})"
        )
