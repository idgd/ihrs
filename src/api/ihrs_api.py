"""ihrs api"""
# pylint: disable-msg=C0103, C0301

import pymongo

from bson.objectid import ObjectId

DATABASE_NAME = "ihrs"
DATABASE_COLLECTION_NAME = ["messages"]

class DatabaseConnection():
    """doc string"""

    def __init__(self):
        """doc string"""
        self.db = self.connect()

    def connect(self):
        """docstring"""

        client = pymongo.MongoClient()
        databaseName = DATABASE_NAME
        db = client.get_database(databaseName)

        return db

    def read(self, messageID=""):
        """docstring"""

        messageText = self.db.get_collection(DATABASE_COLLECTION_NAME[0]).find_one({"_id" : ObjectId(messageID)})

        return messageText

    def return_list(self):
        """docstring"""

        listOfRecords = self.db.get_collection(DATABASE_COLLECTION_NAME[0]).find()

        return listOfRecords
