#!/usr/bin/python3

import random
import time

def generateRandomRow(uniq: int):
    """
    Generate a Random Row of Spotify Music to quickly mock the database

    Sample Usage:
        >>> from mock_db import data
        >>> from pprint import pprint
        >>> len(data)
        170654
        >>> pprint(data[0])
        {'acousticness': 0.026367798980494794,
         'artists': ['artist_3', 'artist_8', 'artist_10', 'artist_5'],
         'danceability': 0.10143790569203848,
         'duration_ms': 8556200,
         'energy': 0.6838281192359255,
         'explicit': 1,
         'id': 'song0_1676959706.2067766',
         'instrumentalness': 0.7162367697208569,
         'valence': 0.034946914615498814,
         'year': 1953}
        >>>

    Args:
        uniq (int): A unique integer to ensure there are no duplicate song ids

    Returns:
        dict: A mock database entry

    """
    return {
        "id": "song" + str(uniq) + "_" + str(time.time()),
        "valence": random.uniform(0,1),
        "year": random.randint(1950, 2023),
        "acousticness": random.uniform(0,1),
        "artists": list(set([f"artist_{random.randint(1, 10)}" for i in range(random.randint(1,5))])),
        "danceability": random.uniform(0,1),
        "duration_ms": random.randint(1316, 17040000),
        "energy": random.uniform(0,1),
        "explicit": 1 if random.uniform(0,1) >= 0.5 else 0,
        "instrumentalness": random.uniform(0,1)
    }


data = [generateRandomRow(i) for i in range(170654)]
