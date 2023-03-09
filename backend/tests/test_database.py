from firebase_admin import firestore
from random import randrange

from backend_imports import database
from backend_imports import dbutils

TEST_COLLECTION = 'test'
TEST_DICT = {
    'test': "test_entry",
}

database._setup_database()

def add_test_document(d: dict):
    """
    Helper for adding a test document

    Args:
        d (dict): a test document to be added

    Returns:
        (str) a key for the document that was added
    """
    key = str(randrange(100, 1000))
    dbutils.add_document(TEST_COLLECTION, key, d)
    return key

def get_test_document(key):
    """
    Helper for getting a test document

    Args:
        key (str): a key for the test document to retrieve

    Returns:
        (dict) a dictionary containing the document for said `key`
    """
    return dbutils.get_document(TEST_COLLECTION, key)

def delete_test_document(key):
    """
    Helper for deleting the test document

    Args:
        key (str): the key for the test document
    """
    dbutils.delete_document(TEST_COLLECTION, key)

def test_add_test_document():
    """
    Tests adding, getting, and deleting a document in firestore
    """
    id = add_test_document(TEST_DICT)
    res = get_test_document(id)
    assert TEST_DICT == res, "The two test documents are not the same"

    delete_test_document(id)
    assert get_test_document(id) == None, "The test document was not deleted"
