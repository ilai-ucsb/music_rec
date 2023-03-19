#!/usr/bin/python3

import csv
import logging
import os, sys
import pandas as pd
from pprint import pprint
import time

from limits import VALIDATION_TABLE

logger = logging.getLogger(__name__)  # get the logger from the callee

PRODUCTION = os.environ.get("PRODUCTION", "0")

rootDir = os.path.dirname(__file__)
raw_data = os.path.join(rootDir, 'raw_data.csv')

if int(PRODUCTION) == 0:  # if we are not in production, then use the mock database
    from mock_db import get_data
    data = get_data(seed=0)
else:  # if we are in production mode, then use the firebase database
    with open(raw_data, encoding="utf-8") as f:
        csvReader = csv.DictReader(f)
        data = [row for row in csvReader]

VERBOSE = bool(int(os.environ.get("VERBOSE", "0")))


# the columns to preprocess to between 0 and 1, inclusive on both ends
NUMERIC_PREPROCESSING_COLUMNS = [
    "year",
    "duration_ms",
    "key",
    "loudness",
    "popularity",
    "tempo",
]


def processTypes(data: pd.DataFrame):
    """
    Casts type of each column using the Validation Table

    Args:
        data (pd.DataFrame): the raw data in form of pandas dataframe

    Returns:
        (pd.DataFrame): a pandas dataframe with the correct types for each column
    """
    for column in VALIDATION_TABLE.keys():
        if column in data.columns:
            data[column] = data[column].astype(VALIDATION_TABLE[column]["expected_type"])
    return data


def preprocessNumeric(column_name: str, column_data: pd.Series):
    """
    Generate a scaled column of the same shape as column_data to ensure all data is between 0 and 1, inclusive.

    Args:
        column_name (str): The name of the column for which a key exists in VALIDATION_TABLE
        column_data (pd.Series | int | float): The data of the column to preprocess

    Returns:
        (pd.Series | float): A pandas Series containing the scaled values of column_data
    """
    minimum = VALIDATION_TABLE[column_name]["minimum"]
    maximum = VALIDATION_TABLE[column_name]["maximum"]
    difference = maximum - minimum
    return (column_data - minimum) / difference


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
    if expected_type == int and type(value) != expected_type:
        return False
    elif expected_type == float and type(value) not in (float, int):
        return False
    if value < minimum:
        return False
    if value > maximum:
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
        if VALIDATION_TABLE[column_name]["expected_type"] in (int, float):
            if not validateNumeric(value=column_value, **VALIDATION_TABLE[column_name]):
                return False

    return True


def similarSongs(n: int = 5, threshold: float = 0.1, **kwargs):
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
            tempo (int): an integer between 0 and 1015, inclusive on both ends

    Returns:
        (list[dict]): A list of three songs with features provided as a dictionary
    """
    logger.debug(f"similar_songs: Received Input n=`{n}` and kwargs=`{kwargs}`.")
    logger.debug("Checking Validity of parameters...")
    # check if there are any bad keys
    bad_keys = kwargs.keys() - VALIDATION_TABLE.keys()
    if len(bad_keys) > 0:
        raise ValueError(f"Incorrect key(s) {bad_keys}")
    if not (n >= 1 and type(n) == int):
        raise ValueError("Incorrect input value for `n` (Count of results to return)")  # raise ValueError on ill-formed args
    if len(kwargs) == 0:
        raise RuntimeError("Did not find any arguments. Did you specify any arguments when attempting to find similarSongs?")  # raise RuntimeError when no kwargs are passed
    if not validateArgs(kwargs):
        raise ValueError("Incorrect format for one of the keyword arguments.")  # raise ValueError on ill-formed args

    logger.debug("Parameters have passed validity checks")
    original = processTypes(pd.DataFrame(data))

    dbObj = processTypes(pd.DataFrame(data)[kwargs.keys()])

    for column_name in kwargs.keys():
        if column_name in NUMERIC_PREPROCESSING_COLUMNS:
            dbObj[column_name] = preprocessNumeric(column_name, dbObj[column_name])
            kwargs[column_name] = preprocessNumeric(column_name, kwargs[column_name])

    dbObj["idx"] = dbObj.index
    logger.debug(dbObj)  # display some rows and columns in the database in debug mode

    for column_name, column_value in kwargs.items():
        tmp = dbObj[[column_name]]
        result = dbObj[abs((tmp - {column_name: column_value}).sum(axis=1)) <= threshold]
        dbObj = dbObj.merge(result, how="inner", indicator=False)

    # sort the database based on the sum over axis 1 (row-based sum)
    dbObj["total"] = abs((dbObj[kwargs.keys()] - kwargs).sum(axis=1))
    dbObj.loc[dbObj["total"].sort_values().index]

    # get the first five values and return them in a record format
    idxs = dbObj[:n]["idx"]
    return (original.iloc[idxs])[["name", "id"]].to_dict(orient='records')


if __name__ == "__main__":
    logger.setLevel(logging.DEBUG if VERBOSE else logging.INFO)
    logger.debug("Running local tests for similarity_songs")
    result = validateArgs(
        {
            "valence": 0.5,
            "year": 2023
        }
    )
    print(result)
    pprint(similarSongs(valence=0.5))
