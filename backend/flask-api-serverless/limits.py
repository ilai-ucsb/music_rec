#!/usr/bin/python3

# hold all the minimum, maximum, and expected type information for all the numeric columns in the table
# for verification of input data
VALIDATION_TABLE = {
    "valence": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": float
    },
    "year": {
        "minimum": 1920,
        "maximum": 2023,
        "expected_type": int
    },
    "acousticness": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": float
    },
    "danceability": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": float
    },
    "duration_ms": {
        "minimum": 1316,
        "maximum": 17040000,
        "expected_type": int
    },
    "energy": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": float
    },
    "explicit": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": int
    },
    "instrumentalness": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": float
    },
    "key": {
        "minimum": 0,
        "maximum": 11,
        "expected_type": int
    },
    "liveness": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": float
    },
    "loudness": {
        "minimum": -60,
        "maximum": 10,
        "expected_type": float
    },
    "mode": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": int
    },
    "popularity": {
        "minimum": 0,
        "maximum": 100,
        "expected_type": int
    },
    "speechiness": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": float
    },
    "tempo": {
        "minimum": 0,
        "maximum": 1015,
        "expected_type": float
    },
}
