#!/usr/bin/python3

import random
import time


def generateRandomDate():
    """
    Return a valid random date between January 1st, 1950 and December 31st, 2023

    Returns:
        str: A valid date formatted as YYYY-mm-dd
    """
    earliest_date = time.mktime((1950,1,1,0,0,0,0,0,0))  # January 1st, 1950, 12 AM
    latest_date = time.mktime((2023,12,31,0,0,0,0,0,0))  # December 31st, 2023, 12 AM
    date_difference = latest_date - earliest_date
    random_date = time.gmtime(random.random() * date_difference + earliest_date)
    return time.strftime("%Y-%m-%d", random_date)


def generateRandomRow(uniq: int):
    """
    Generate a Random Row of Spotify Music to quickly mock the database

    Sample Usage:
        >>> from mock_db import data
        >>> from pprint import pprint
        >>> len(data)
        170654
        >>> pprint(data[0])
        {'acousticness': 0.44734290491938256,
         'artists': ['artist_5'],
         'danceability': 0.03975210984781774,
         'duration_ms': 15194458,
         'energy': 0.8371572141671999,
         'explicit': 0,
         'id': 'song0_1676966597.8889136',
         'instrumentalness': 0.8419190390078436,
         'key': 8,
         'liveness': 0.9299395681349847,
         'loudness': 0.6637308653381392,
         'loudness_raw': 9.420488898718531,
         'mode': 0,
         'name': 'songname-0',
         'popularity': 0.008840186354381108,
         'popularity_raw': 2,
         'release_date': '1983-06-27',
         'tempo': 167.1795553881779,
         'valence': 0.5158085156007629,
         'year': 1983}
        >>>

    Args:
        uniq (int): A unique integer to ensure there are no duplicate song ids

    Returns:
        dict: A mock database entry

    """
    random_date = generateRandomDate()
    return {
        "id": "song" + str(uniq) + "_" + str(time.time()),
        "valence": random.uniform(0,1),
        "year": int(random_date[:4]),  # let's hard code the limit for the max year to 2023
        "acousticness": random.uniform(0,1),
        "artists": list(set([f"artist_{random.randint(1,10)}" for i in range(random.randint(1,5))])),
        "danceability": random.uniform(0,1),
        "duration_ms": random.randint(1316,17040000),  # likely we won't get duration lower than 1.316 seconds and longer than 4.73 hours
        "energy": random.uniform(0,1),
        "explicit": 1 if random.uniform(0,1) >= 0.5 else 0,
        "instrumentalness": random.uniform(0,1),
        "key": random.randint(0,11),
        "liveness": random.uniform(0,1),
        "loudness_raw": random.uniform(-60,10),  # likely we won't get loudness above 3.855
        "loudness": random.uniform(0,1),
        "mode": 1 if random.uniform(0,1) >= 0.5 else 0,
        "name": f"songname-{uniq}",
        "popularity_raw": random.randint(0,100),
        "popularity": random.uniform(0,1),
        "release_date": random_date,
        "tempo": random.uniform(0,1015)  # likely we won't get tempo above 1015
    }


data = [generateRandomRow(i) for i in range(170654)]
