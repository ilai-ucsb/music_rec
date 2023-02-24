# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:28:28 2023
@author: Parsa Hafezi
"""

from mock_db import generateRandomRow
from backend_imports import getLoud

"""test get loud song with one song"""

def test_1():
    data = [
                {"acousticness": 0.44734290491938256,
                 "artists": ["artist_5"],
                 "danceability": 0.03975210984781774,
                 "duration_ms": 15194458,
                 "energy": 0.8371572141671999,
                 "explicit": 0,
                 "id": "song0_1676966597.8889136",
                 "instrumentalness": 0.8419190390078436,
                 "key": 8,
                 "liveness": 0.9299395681349847,
                 "loudness": 0.6637308653381392,
                 "loudness_raw": 9.420488898718531,
                 "mode": 0,
                 "name": "songname-0",
                 "popularity": 0.008840186354381108,
                 "popularity_raw": 2,
                 "release_date": "1983-06-27",
                 "tempo": 167.1795553881779,
                 "valence": 0.5158085156007629,
                 "year": 1983}
            ]
    sorted_data = getLoud(data, 0, 1)
    
    print(sorted_data[0]["id"])
    if(sorted_data[0]["id"] =="song0_1676966597.8889136" ):
        correct = True
    else :
        correct = False
    return correct

"""
Test 3 
test 10 songs, loud = 0, num = 6
expected return should bottom 6 loudest songs in increasing order 
"""
def test_2():
    data = [generateRandomRow(i) for i in range(10)]
    sorted_data = getLoud(data, 0, 6)

    for i in range(5):    
        if(sorted_data[i]["loudness"] <= sorted_data[i+1]["loudness"] ):
            correct = True
        else :
            correct = False
    return correct

"""
Test 3 
test 10 songs, loud = 1, num = 6
expected return should top 6 loudest songs in decreasing order 
"""
def test_3():
    data = [generateRandomRow(i) for i in range(10)]
    sorted_data = getLoud(data, 1, 6)
    
    for i in range(5):    
        if(sorted_data[i]["loudness"] >= sorted_data[i+1]["loudness"] ):
            correct = True
        else :
            correct = False
    return correct

"""
Test 3 
test 10 songs, loud = .5, num = 6
expected return should 6 medium loudest songs in increasing order by distance from .5
"""
def test_4():
    data = [generateRandomRow(i) for i in range(10)]
    sorted_data = getLoud(data, .5, 6)

    for i in range(5):    
        if(abs(sorted_data[i]["loudness"] - .5) <= abs(sorted_data[i+1]["loudness"] - .5) ):
            correct = True
        else :
            correct = False
    return correct
