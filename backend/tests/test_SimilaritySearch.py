#!/usr/bin/python3

import logging
import os
import pandas as pd
import pytest
import sys

os.environ["VERBOSE"] = "0"
os.environ["PRODUCTION"] = "0"

logging.basicConfig(level=logging.CRITICAL)  # don't even warn about errors

from backend_imports import SimilaritySearch


def test_similarSongs_with_n_0():
    inpt = {"n": 0}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    with pytest.raises(ValueError):
        result = SimilaritySearch.similarSongs(**inpt)


def test_similarSongs_with_n_1():
    inpt = {"n": 1}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    with pytest.raises(RuntimeError):
        result = SimilaritySearch.similarSongs(**inpt)


def test_similarSongs_with_n_1_valence():
    inpt = {"n": 1, "valence": 0.5}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    result = SimilaritySearch.similarSongs(**inpt)
    logging.info(f"Call returned {len(result)} rows.")
    assert (
        len(result) == inpt["n"]
    ), f"Length parameter n ({inpt['n']}) returned {len(result)} responses"
    # assert (
    #     result[0]["valence"] >= inpt["valence"] - 0.05
    # ), "Result was below the threshold"
    # assert (
    #     result[0]["valence"] <= inpt["valence"] + 0.05
    # ), "Result was above the threshold"


def test_similarSongs_with_n_5_year():
    inpt = {"n": 5, "year": 2023}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    result = pd.DataFrame(SimilaritySearch.similarSongs(**inpt))
    logging.info(f"Call returned {len(result)} rows.")
    assert (
        len(result) == inpt["n"]
    ), f"Length parameter n ({inpt['n']}) returned {len(result)} responses"
    # for original, sortd in zip(result["year"].tolist(), result["year"].sort_values(ascending=False).tolist()):
    #     assert (
    #         original == sortd
    #     ), f"Year was not returned in descending order from {inpt['year']}"


def test_similarSongs_with_n_2_acousticness_danceability_duration_ms_energy():
    inpt = {
        "n": 2,
        "acousticness": 0.5,
        "danceability": 0.5,
        "duration_ms": 10000,
        "energy": 0.5,
    }
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    result = pd.DataFrame(SimilaritySearch.similarSongs(**inpt))
    logging.info(f"Call returned {len(result)} rows.")
    assert (
        len(result) <= inpt["n"]
    ), f"Length parameter n ({inpt['n']}) returned {len(result)} responses"


def test_similarSongs_with_n_2_explicit_instrumentalness():
    inpt = {"n": 2, "explicit": 0, "instrumentalness": 1.0}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    result = pd.DataFrame(SimilaritySearch.similarSongs(**inpt))
    logging.info(f"Call returned {len(result)} rows.")
    assert (
        len(result) <= inpt["n"]
    ), f"Length parameter n ({inpt['n']}) returned {len(result)} responses"
    # assert (
    #     result["explicit"].sum() == 0
    # ), f"{inpt} returned\n{result}\nwhich had some explicit songs"


def test_similarSongs_with_n_2_key_liveness_loudness_mode():
    inpt = {"n": 2, "key": 11, "liveness": 1.0, "loudness": -14.0, "mode": 1}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    result = pd.DataFrame(SimilaritySearch.similarSongs(**inpt))
    logging.info(f"Call returned {len(result)} rows.")
    assert (
        len(result) <= inpt["n"]
    ), f"Length parameter n ({inpt['n']}) returned {len(result)} responses"


def test_similarSongs_with_n_2_popularity_tempo():
    inpt = {"n": 2, "popularity": 100, "tempo": 120}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    result = pd.DataFrame(SimilaritySearch.similarSongs(**inpt))
    logging.info(f"Call returned {len(result)} rows.")
    assert (
        len(result) <= inpt["n"]
    ), f"Length parameter n ({inpt['n']}) returned {len(result)} responses"


def test_similarSongs_invalid_input_1():
    inpt = {"mode": 0.2}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    with pytest.raises(ValueError):
        result = SimilaritySearch.similarSongs(**inpt)


def test_similarSongs_invalid_input_2():
    inpt = {"year": 1917}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    with pytest.raises(ValueError):
        result = SimilaritySearch.similarSongs(**inpt)


def test_similarSongs_invalid_input_3():
    inpt = {"explicit": 0.5}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    with pytest.raises(ValueError):
        result = SimilaritySearch.similarSongs(**inpt)


def test_similarSongs_invalid_input_4():
    inpt = {"popularity": 111}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    with pytest.raises(ValueError):
        result = SimilaritySearch.similarSongs(**inpt)


def test_similarSongs_invalid_input_5():
    inpt = {"tempo": 10000.0}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    with pytest.raises(ValueError):
        result = SimilaritySearch.similarSongs(**inpt)


def test_similarSongs_invalid_input_6():
    inpt = {"duration_ms": 27040000}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    with pytest.raises(ValueError):
        result = SimilaritySearch.similarSongs(**inpt)


def test_similarSongs_invalid_input_7():
    inpt = {"loudness": 14}
    logging.info(
        f"Testing Similar Songs Algorithm with {' & '.join([f'{k}={v}' for k, v in inpt.items()])}"
    )
    with pytest.raises(ValueError):
        result = SimilaritySearch.similarSongs(**inpt)
