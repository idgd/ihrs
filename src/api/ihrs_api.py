"""ihrs api"""
# pylint: disable-msg=C0103

import pymongo

from bson.objectid import ObjectId

class DatabaseConnection():
    """doc string"""

    def __init__(self):
        """doc string"""

    def connect(self):
        """docstring"""

        client = pymongo.MongoClient()
        db = client.ihrs
        return db

    def read(self, db, a):
        """docstring"""

        return db.messages.find_one({"_id" : ObjectId(a)})

    def return_list(self, db):
        """docstring"""

        ret = []
        idList = db.messages.inserted_ids()
        for f in idList:
            ret.append(str(f))

        return ret
