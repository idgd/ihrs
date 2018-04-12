import pymongo
import json
from inovonics.echostream.messages.serial import decodeSerialMessage
from bson.objectid import ObjectId

DATABASE_NAME = "ihrs"
DATABASE_COLLECTION_NAME = ["messages"]

class DatabaseConnection():

    def __init__(self):
        self.db = self.connect()

    def connect(self):
        client = pymongo.MongoClient('138.86.104.164',27017)
        database_name = DATABASE_NAME
        db = client.get_database(database_name)

        return db

    def read(self, messageID=""):
        message_text = self.db.get_collection(DATABASE_COLLECTION_NAME[0]).find_one({"_id" : ObjectId(messageID)})

        return message_text

    def return_list(self):
        list_of_records = self.db.get_collection(DATABASE_COLLECTION_NAME[0]).find()

        return list_of_records

    def add_message(self,in_bytes):
        json_message = decodeSerialMessage(in_bytes)
        new_message = self.db.insert(json_message)
