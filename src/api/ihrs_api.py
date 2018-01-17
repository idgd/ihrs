"""ihrs api"""
# pylint: disable-msg=C0103, C0301

import pymongo

from bson.objectid import ObjectId

DATABASE_NAME = "ihrs"
DATABASE_COLLECTION_NAME = ["messages"]

class DatabaseConnection():
    """this class stores the database and has some database methods"""

    def __init__(self):
        """initializes database and connects"""
        self.db = self.connect()

    def connect(self):
        """connects database to the DATABASE_NAME"""

        client = pymongo.MongoClient()
        databaseName = DATABASE_NAME
        db = client.get_database(databaseName)

        return db

    def read(self, messageID=""):
        """takes in a message ID string and returns the document in the database"""

        messageText = self.db.get_collection(DATABASE_COLLECTION_NAME[0]).find_one({"_id" : ObjectId(messageID)})

        return messageText

    def return_list(self):
        """returns the records in the database records"""

        listOfRecords = self.db.get_collection(DATABASE_COLLECTION_NAME[0]).find()

        return listOfRecords
