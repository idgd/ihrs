import pymongo
import json
import inovonics

from inovonics.echostream.messages.serial import decodeSerialMessage
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

        client = pymongo.MongoClient('138.86.104.164',27017)
        database_name = DATABASE_NAME
        db = client.get_database(database_name)

        return db

    def read(self, messageID=""):
        """takes in a message ID string and returns the document in the database"""

        message_text = self.db.get_collection(DATABASE_COLLECTION_NAME[0]).find_one({"_id" : ObjectId(messageID)})

        return message_text

    def return_list(self):
        """returns the records in the database records"""

        list_of_records = self.db.get_collection(DATABASE_COLLECTION_NAME[0]).find()

        return list_of_records

    def add_message(self,in_bytes):
        """adds record to the messages collection"""

        json_message = decodeSerialMessage(in_bytes)
        new_message = self.db.insert(json_message)
