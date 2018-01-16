"""ihrs api"""

import json
import pymongo

from bson.objectid import ObjectId

def connect():
    """docstring"""

    client = pymongo.MongoClient()
    db = client.local
    return db

def read(db, a):
    """docstring"""

    return db.messages.find_one({"_id" : ObjectId(a)})

def return_list(db):
    """docstring"""

    return db.messages.inserted_ids
