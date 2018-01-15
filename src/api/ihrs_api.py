import pymongo
import json
from bson.objectid import ObjectId

#TODO make database conenction
def connect():
	client = pymongo.MongoClient()
	db = client.local
	return(db)

#TODO make method for reading records on database
def read(db,a):
	return(json.dumps(db.messages.find_one({"_id" : ObjectId(a)})))

#TODO possibly make a schema for messages
