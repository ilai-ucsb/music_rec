#!/usr/bin/python3

import logging
import os
import sys


VERBOSE = os.environ.get("VERBOSE", False)

logger = logging.getLogger(__name__)  # get the logger from the callee

PROJECT_NAME = "project-t09-musicrecommendation"  # folder name of the repository

try:
    split_path = __file__.split("/")
    backend_path = "/".join(split_path[:len(split_path) - split_path[::-1].index(PROJECT_NAME)]) + "/backend"
    sys.path.append(backend_path)
    sys.path.append(backend_path + "/flask-api-serverless")
except ValueError as ve:
    logger.error(f"There was an issue retrieving the folder path to the backend. Ensure the folder {PROJECT_NAME} is a substring of your current path in the filesystem.")
    logger.error(ve)
    raise  # re-raise the error to stop execution
except Exception as exc:
    logger.error(f"An unexpected error occurred.")
    logger.error(exc)
    raise  # re-raise the error to stop execution


# all the setup has been done to import modules. Now you can import modules in the try-except block below

try:
    # add your imports here
    import SimilaritySearch
    import loud

except ModuleNotFoundError as mnfe:
    logger.error(f"Error when importing a module. Is the file in either of the following folders: {sys.path}")
    logger.error(mnfe)
    raise  # re-raise to stop execution
except Exception as exc:
    logger.error("An unexpected error occurred.")
    logger.error(exc)
    raise  # re-raise to stop execution
