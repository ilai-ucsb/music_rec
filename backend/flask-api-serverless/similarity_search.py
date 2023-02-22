#!/usr/bin/python3

import logging
import os
import pandas as pd
from pprint import pprint
import time

PRODUCTION = os.environ.get("PRODUCTION", False)

if not PRODUCTION:  # if we are not in production, then use the mock database
    import sys

    PROJECT_NAME = "project-t09-musicrecommendation"

    try:
        data_path = "/".join(__file__.split("/")[:__file__.split("/").index(PROJECT_NAME)+1]) + "/data"
    except ValueError as ve:
        logging.error(f"There was an issue deriving the data path for the mock database. Ensure the folder {PROJECT_NAME} is a substring of your current path in the filesystem.")
        logging.error(ve)
        raise  # re-raise the error to stop execution
    except Exception as exc:
        logging.error("An unexpected error occurred.")
        logging.error(exc)
        raise  # re-raise the error to stop execution

    sys.path.append(data_path)
    from mock_db import get_data
    data = get_data(seed=0)
else:  # if we are in production mode, then use the firebase database
    pass

VERBOSE = os.environ.get("VERBOSE", False)


VALIDATION_TABLE = {
    "valence": {
        "minimum": 0,
        "maximum": 1,
        "expected_type": float
    },
    "year": {
        "minimum": 1950,
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
    "release_date": {
        "expected_type": str,
        "_format": "%Y-%m-%d",
        "year_col": "year"
    },
    "tempo": {
        "minimum": 0,
        "maximum": 1015,
        "expected_type": int
    },
}


def validateNumeric(value, minimum, maximum, expected_type):
    """
    Helper function to validate the numeric input `value` and ensure
    that it is in between `minimum` and `maximum` while being of the correct
    `expected_type`.

    Args:
        value (int | float): A value of either int type or float type to validate
        minimum (int | float): The minimum numeric value that the value can be
        maximum (int | float): The maximum numeric value that the value can be
        expected_type (type): Either `int` or `float` to validate the type of value

    Returns:
        (bool): True if valid else False
    """
    if type(value) != expected_type:
        return False
    if value < minimum:
        return False
    if value > maximum:
        return False
    return True


def validateDate(value: str, _format: str = "%Y-%m-%d", year: int = None, expected_type: type = str):
    """
    Helper function to validate the string input `value` representing the date and ensure
    that it is in the correct format while having the correct year.

    Args:
        value (str): The date string in format `_format`
        _format (str): The format to expect the value to be in. Default "%Y-%m-%d" (eg, "2023-08-15" for August 15th, 2023)
        year (int): The expected year for the date

    Returns:
        (bool): True if valid else False
    """
    if type(value) != str:
        return False
    try:
        date = time.strptime(value, _format)
    except ValueError as ve:
        logging.debug(f"An error occurred trying to parse the date field with format \"{fmt}\". This implies that the field is not valid.")
        logging.debug(ve)
        return False
    except Exception as exc:
        logging.error("An unexpected error occurred trying to parse \"{value}\" with format \"{fmt}\". See below for more details.")
        logging.error(exc)
        return False

    if year and date.tm_year != year:
        return False
    return True


def validateArgs(kwargs: dict):
    """
    Validates all the keyword arguments as described in the definition for the
    `similar_songs` function.

    Args:
        kwargs (dict): All the arguments defined in `similar_songs`

    Returns:
        (bool): True if all arguments are valid else False
    """
    for column_name, column_value in kwargs.items():
        if VALIDATION_TABLE[column_name]["expected_type"] == str and "date" in column_name:
            if not validateDate(value=column_value, _format=VALIDATION_TABLE[column_name]["_format"], year=kwargs.get(VALIDATION_TABLE[column_name]["year_col"], None)):
                return False
        if VALIDATION_TABLE[column_name]["expected_type"] in (int, float):
            if not validateNumeric(value=column_value, **VALIDATION_TABLE[column_name]):
                return False

    return True


def similarSongs(n: int = 5, threshold: float = 0.05, **kwargs):
    """
    Finds the Top `n` similar tracks given a set of feature suggestions.

    Note that all arguments will be validated. The following arguments are
    acceptable with this function:
    Args:
        n (int): The number of results to return
        kwargs:
            valence (float): a decimal between 0 and 1
            year (int): an integer between 1950 and 2023, inclusive on both ends
            acousticness (float): a decimal between 0 and 1
            danceability (float): a decimal between 0 and 1
            duration_ms (int): an integer between 1316 and 17040000, inclusive on both ends
            energy (float): a decimal between 0 and 1
            explicit (int): either 1 or 0
            instrumentalness (float): a decimal between 0 and 1
            key (int): an integer between 0 and 11, inclusive on both ends
            liveness (float): a decimal between 0 and 1
            loudness (float): a decimal between -60 dB and 10 dB, inclusive on both ends
            mode (int): either 1 or 0
            popularity (int): an integer between 0 and 100, inclusive on both ends
            release_date (str): a valid date with the ear being identical to the year value if provided
            tempo (int): an integer between 0 and 1015, inclusive on both ends

    Returns:
        (list[dict]): A list of three songs with features provided as a dictionary
    """
    logging.debug(f"similar_songs: Received Input n=`{n}` and kwargs=`{kwargs}`.")
    logging.debug("Checking Validity of parameters...")
    if not (n >= 1 and type(n) == int):
        logging.error("Incorrect input value for `n` (Count of results to return)")
        return None  # return None on error
    if not validateArgs(kwargs):
        logging.error("Incorrect format for one of the keyword arguments.")
        return None

    logging.debug("Parameters have passed validity checks")
    dbObj = pd.DataFrame(data)[kwargs.keys()]
    dbObj["idx"] = dbObj.index
    logging.debug(dbObj)  # display some rows and columns in the database in debug mode

    for column_name, column_value in kwargs.items():
        tmp = dbObj[[column_name]]
        result = dbObj[abs((tmp - {column_name: column_value}).sum(axis=1)) <= threshold]
        dbObj = dbObj.merge(result, how="inner", indicator=False)

    idxs = dbObj[:5]["idx"]
    original = pd.DataFrame(data)
    return original.iloc[idxs].to_dict(orient='records')


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG if VERBOSE else logging.INFO)
    logging.debug("Running local tests for similarity_songs")
    result = validateArgs(
        {
            "valence": 0.5,
            "year": 2023,
            "release_date": "2023-10-15"
        }
    )
    print(result)
    pprint(similarSongs(liveness=0.3, tempo=120, threshold=15))
