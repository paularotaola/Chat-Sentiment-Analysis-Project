#from app import app
from pymongo import MongoClient
from src.config import DBURL
from bson.objectid import ObjectId

from flask import Flask

app = Flask(__name__)

client = MongoClient()
print(f"connected to {client}")
db = client.get_database("My-Super-API")


def addUser(name):
    """Checks if the user already exists and adds it to the database"""

    if len(list(db.users.find({"name": { "$eq": f"{name}" } })) )>0:
        print("The User already exists")

    else:
        output = db.users.insert_one ({
        "name": f"{name}"}).inserted_id
        return output

def addConversation(chat):
    """Checks if the group already exists and adds it to the database"""
    coll_chat = db['conversations']
    conversation = coll_chat.insert_one({
         "conversation_group": chat
    }).inserted_id
    return f"New group created!. Id: {str(conversation)}"