#!/usr/bin/python3

import logging
import os
import sys


VERBOSE = os.environ.get("VERBOSE", False)

logging.basicConfig(level=logging.DEBUG if VERBOSE else logging.INFO)

PROJECT_NAME = "project-t09-musicrecommendation"  # folder name of the repository

try:
    split_path = __file__.split("/")
    backend_path = "/".join(split_path[:len(split_path) - split_path[::-1].index(PROJECT_NAME)]) + "/backend"
    sys.path.append(backend_path)
    sys.path.append(backend_path + "/flask-api-serverless")
except ValueError as ve:
    logging.error(f"There was an issue retrieving the folder path to the backend. Ensure the folder {PROJECT_NAME} is a substring of your current path in the filesystem.")
    logging.error(ve)
    raise  # re-raise the error to stop execution
except Exception as exc:
    logging.error(f"An unexpected error occurred.")
    logging.error(exc)
    raise  # re-raise the error to stop execution

try:
    # add your imports here
    from SimilaritySearch import similarSongs

except ModuleNotFoundError as mnfe:
    logging.error(f"Error when importing a module. Is the file in either of the following folders: {sys.path}")
    logging.error(mnfe)
    raise  # re-raise to stop execution
except Exception as exc:
    logging.error("An unexpected error occurred.")
    logging.error(exc)
    raise  # re-raise to stop execution
