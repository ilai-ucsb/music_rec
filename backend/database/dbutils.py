from firebase_admin import firestore
from random import randrange

import database
import dbconfig


def add_document(c_name, d_key, d_val):
    db = firestore.client()
    collection = db.collection(c_name)
    collection.document(d_key).set(d_val)

def get_document(c_name, d_key):
    db = firestore.client()
    collection = db.collection(c_name)
    doc = collection.document(d_key)
    return doc.get().to_dict()

def delete_document(c_name, d_key):
    db = firestore.client()
    collection = db.collection(c_name)
    doc = collection.document(d_key)
    doc.delete()
