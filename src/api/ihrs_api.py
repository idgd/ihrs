import pymongo

#TODO make database conenction
def connect():
	client = pymongo.MongoClient()
	db = client.local
	return(db)

#TODO make method for reading records on database
def read(db,a):
	return(db.messages.find_one({"_id" : a}))

#TODO possibly make a schema for messages
