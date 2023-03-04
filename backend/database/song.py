class Song(object):
    # popular songs
    GANGNAM_STYLE = "Gangnam Style"
    DESPACITO = "Despacito"
    INVALID_SONG = "nbdjs183hdjhkzxiuoq2uqejhsjhks"
    
    # SPOTIFY_API_GOLDEN_COLUMNS: set of strings used for testing
    SPOTIFY_API_GOLDEN_COLUMNS = ('id', 'name', 'year',
                                  'explicit', 'duration_ms',
                                  'popularity', 'danceability',
                                  'energy', 'key','loudness',
                                  'mode', 'speechiness',
                                  'acousticness','instrumentalness',
                                  'liveness', 'valence',
                                  'tempo', 'time_signature')
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
    def __init__(self, id, name, popularity, year, artists, danceability, 
                 acousticness, energy, explicit, instrumentalness, liveness, 
                 loudness, speechiness, tempo, artist_pop=0, genres=[]):
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

    @staticmethod
    def from_dict(source):
        song = Song(source[u'id'], source[u'name'], source[u'popularity'], 
                    source[u'year'], source[u'artists'], source[u'danceability'], 
                    source[u'acousticness'], source[u'energy'], source[u'explicit'], 
                    source[u'instrumentalness'], source[u'liveness'], 
                    source[u'loudness'], source[u'speechiness'], source[u'tempo'])
        if u'genres' in source:
            song.genres = source[u'genres']
        if u'artist_pop' in source:
            song.artist_pop = source[u'artist_pop']
        return song

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
