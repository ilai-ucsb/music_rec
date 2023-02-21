import database
import config

from firebase_admin import firestore
from random import randrange

def add_document(c_name, d_key, d_val):
    db = firestore.client()
    collection = db.collection(c_name)
    collection.document(d_key).set(d_val)

def add_test_document(dict):
    collection = config.TEST_COLLECTION
    key = str(randrange(100,1000))
    add_document(collection, key, dict)
    return key

def get_document(c_name, d_key):
    db = firestore.client()
    collection = db.collection(c_name)
    doc = collection.document(d_key)
    return doc.get().to_dict()

def get_test_document(key):
    collection = config.TEST_COLLECTION
    return get_document(collection, key)

def delete_document(c_name, d_key):
    db = firestore.client()
    collection = db.collection(c_name)
    doc = collection.document(d_key)
    doc.delete()

def delete_test_document(key):
    collection = config.TEST_COLLECTION
    delete_document(collection, key)


def test_add_test_document():
    id = add_test_document(config.TEST_DICT)
    res = get_test_document(id)
    assert config.TEST_DICT == res, "The two test documents are not the same"
    return id

def test_delete_test_document(key="abc"):
    delete_test_document(key)
    assert get_test_document(key) == None, "The test document was not deleted"




if __name__ == "__main__":
    database._setup_database()
    id = test_add_test_document()
    test_delete_test_document(id)

