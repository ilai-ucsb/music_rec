from backend_imports import popularity, mock_db

"""test get loud song with one song"""


def test_1():
    data = [
        {
            "acousticness": 0.44734290491938256,
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
            "year": 1983,
        }
    ]
    sorted_data = popularity.getPopularity(data, 0, 1)

    assert (
        sorted_data[0]["id"] == "song0_1676966597.8889136"
    ), f"Something went wrong. When comparing {sorted_data[0]['id']} (received) and 'song0_1676966597.8889136' (expected)"


"""
Test 2 
test 10 songs, loud = 0, num = 6
expected return should bottom 6 loudest songs in increasing order 
"""


def test_2():
    data = [mock_db.generateRandomRow(i) for i in range(10)]
    sorted_data = popularity.getPopularity(data, 0, 6)

    for i in range(5):
        assert (
            sorted_data[i]["popularity"] <= sorted_data[i + 1]["popularity"]
        ), f"popularity not sorted right {sorted_data[i]['popularity']} (current) not <= {sorted_data[i+1]['popularity']} (next)"


"""
Test 3 
test 10 songs, loud = 1, num = 6
expected return should top 6 popular songs in decreasing order 
"""


def test_3():
    data = [mock_db.generateRandomRow(i) for i in range(10)]
    sorted_data = popularity.getPopularity(data, 1, 6)

    for i in range(5):
        assert (
            sorted_data[i]["popularity"] >= sorted_data[i + 1]["popularity"]
        ), f"popularity not sorted right {sorted_data[i]['popularity']} (current) not >= {sorted_data[i+1]['popularity']} (next)"


"""
Test 4
test 10 songs, loud = .5, num = 6
expected return should 6 medium popular songs in increasing order by distance from .5
"""


def test_4():
    data = [mock_db.generateRandomRow(i) for i in range(10)]
    sorted_data = popularity.getPopularity(data, 0.5, 6)

    for i in range(5):
        assert abs(sorted_data[i]["popularity"] - 0.5) <= abs(
            sorted_data[i + 1]["popularity"] - 0.5
        ), f"Distance from current ({sorted_data[i]['popularity']}) is further from next ({sorted_data[i+1]['popularity']})"
