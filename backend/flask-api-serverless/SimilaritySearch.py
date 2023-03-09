#!/usr/bin/python3

import csv
import logging
import os, sys
import pandas as pd
from pprint import pprint
import time

from limits import VALIDATION_TABLE

logger = logging.getLogger(__name__)  # get the logger from the callee

PRODUCTION = os.environ.get("PRODUCTION", False)

PROJECT_NAME = "project-t09-musicrecommendation"

try:
    split_path = __file__.split("/")
    data_path = "/".join(split_path[:len(split_path) - split_path[::-1].index(PROJECT_NAME)]) + "/data"
except ValueError as ve:
    logger.error(f"There was an issue deriving the data path for the mock database. Ensure the folder {PROJECT_NAME} is a substring of your current path in the filesystem.")
    logger.error(ve)
    raise  # re-raise the error to stop execution
except Exception as exc:
    logger.error("An unexpected error occurred.")
    logger.error(exc)
    raise  # re-raise the error to stop execution

sys.path.append(data_path)

if int(PRODUCTION) == 0:  # if we are not in production, then use the mock database
    from mock_db import get_data
    data = get_data(seed=0)
else:  # if we are in production mode, then use the firebase database
    with open(data_path + "/raw_data.csv", encoding="utf-8") as f:
        csvReader = csv.DictReader(f)
        data = [row for row in csvReader]

    from database import _setup_database
    _setup_database()
    db = firestore.Client()
    data = list(map(lambda x: x.to_dict(), list(db.collection(u'Songs').stream())))

VERBOSE = os.environ.get("VERBOSE", False)


# the columns to preprocess to between 0 and 1, inclusive on both ends
NUMERIC_PREPROCESSING_COLUMNS = [
    "year",
    "duration_ms",
    "key",
    "loudness",
    "popularity",
    "tempo",
]


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
        logger.debug(f"An error occurred trying to parse the date field with format \"{fmt}\". This implies that the field is not valid.")
        logger.debug(ve)
        return False
    except Exception as exc:
        logger.error("An unexpected error occurred trying to parse \"{value}\" with format \"{fmt}\". See below for more details.")
        logger.error(exc)
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
            tempo (int): an integer between 0 and 1015, inclusive on both ends

    Returns:
        (list[dict]): A list of three songs with features provided as a dictionary
    """
    logger.debug(f"similar_songs: Received Input n=`{n}` and kwargs=`{kwargs}`.")
    logger.debug("Checking Validity of parameters...")
    if not (n >= 1 and type(n) == int):
        raise ValueError("Incorrect input value for `n` (Count of results to return)")  # raise ValueError on ill-formed args
    if len(kwargs) == 0:
        raise RuntimeError("Did not find any arguments. Did you specify any arguments when attempting to find similarSongs?")  # raise RuntimeError when no kwargs are passed
    if not validateArgs(kwargs):
        raise ValueError("Incorrect format for one of the keyword arguments.")  # raise ValueError on ill-formed args

    logger.debug("Parameters have passed validity checks")
    original = pd.DataFrame(data)

    dbObj = pd.DataFrame(data)[kwargs.keys()]

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
    return original.iloc[idxs].to_dict(orient='records')


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
