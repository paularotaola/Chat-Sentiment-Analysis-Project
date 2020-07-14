from pymongo import MongoClient
from src.config import DBURL
#import config as co

client = MongoClient(DBURL)
db = client.get_database()


def checkUser(name):

    if len(list(db.users.find({"name": { "$eq": f"{name}" } })) )>0:
        return True
    else:
        return False

def checkChat(group):
    existe = list(db.coversations.find({"conversation_group": { "$eq": f"{group}" } }))
    if len(existe) == 0:
        return True
    else:
        return False

def userInChat(user,chat):

    if len(list(db.chats.find({ "conversation_group" : f"{chat}", "participants" : f"{user}"})))== 0:
        return False
    else:
        return True