class Song(object):
    """
    The Song object contains all features for each song.

    Arguments:
        - id, (spotify track id)
        - name (string: track name)
        - popularity (double: track popularity)
        - year (integer: track release year)
        - artists (string: track artist name)
        - artist_pop (double: track artist popularity)
        - artist_genres (string[]: track artist genres)
        - danceability (double: between 0 and 1)
        - acouticness (double: between 0 and 1)
        - energy (double: between 0 and 1)
        - explicit (boolean: either 0 or 1)
        - instrumentalness (double: between 0 and 1)
        - liveness (double)
        - loudness (double)
        - speechiness (double)
        - tempo (double)
    """
    def __init__(self, id, name, popularity, year, artists, artist_pop, genres, 
                 danceability, acousticness, energy, explicit, instrumentalness,
                 liveness, loudness, speechiness, tempo):
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

    def to_dict(self):
        dest = {
            u'id': self.id,
            u'name': self.name,
            u'popularity': self.popularity,
            u'artists': self.artists,
            u'artists_pop': self.artist_pop,
            u'danceability': self.danceability,
            u'acousticness': self.acousticness,
            u'energy': self.energy,
            u'explicit': self.explicit.item(),
            u'instrumentalness': self.instrumentalness,
            u'liveness': self.liveness,
            u'loudness': self.loudness,
            u'speechiness': self.speechiness,
            u'tempo': self.tempo
        }
        
        if self.year:
            dest[u'year'] = self.year.item()

        if self.genres:
            dest[u'genres'] = self.genres

        return dest

    def __repr__(self):
        return (
            f'Song(id={self.id}, ' +
            f'name={self.name}, ' +
            f'popularity={self.popularity}, ' +
            f'year={self.year}, ' +
            f'artists={self.artists}, ' +
            f'artist_pop={self.artist_pop}, ' +
            f'genres={self.genres}, ' +
            f'danceability={self.danceability}, ' +
            f'acousticness={self.acousticness}, ' +
            f'energy={self.energy}, ' +
            f'explicit={self.explicit}, ' +
            f'instrumentalness={self.instrumentalness}, ' +
            f'liveness={self.liveness}, ' +
            f'loudness={self.loudness}, ' +
            f'speechiness={self.speechiness}, ' +
            f'tempo={self.tempo})'
        )