from flask import Flask, request
from pymongo import MongoClient
import src.check as c
import src.create as creat
from bson.objectid import ObjectId
import os
import dotenv
dotenv.load_dotenv()
from src.errorHelper import errorHelper, APIError, Error404, checkValidParams
import json


#Inicialización APP:

app = Flask(__name__)
client = MongoClient()
db = client.get_database("My-Super-API")


@app.route('/')
def index():
    return "Hello, World!"


# Crear un usuario
@app.route('/user/create/<name>')

def addUser(name):
    """Checks if the user already exists and adds it to the database"""

    if len(list(db.users.find({"name": { "$eq": f"{name}" } })) )>0:
        print(len(list(db.users.find({"name": { "$eq": f"{name}" } })) )>0)
        return "Sorry. The User already exists"

    else:
        output = creat.addUser(name)
        return f"New user created! id: {str(output)}"


# Crear un chat
@app.route('/chats/create/<chat>')
def crateChats(chat):
    '''
    Creates a group/converstaion (without users) 
    '''

    if len(list(db.conversations.find({"conversation_group": { "$eq": f"{chat}" } })) )>0:
        return "Sorry. The Group already exists"
    
    else:
        conversation = creat.addConversation(chat)
    return f"New group created!. Id: {str(conversation)}"



# Añade un usuario a un chat
@app.route ("/chat/<conversation_id>/adduser")
def user(conversation_id):
    conversation_id = ObjectId(conversation_id)
    new_user = ObjectId(request.args.get("user_id"))
    #print(new_user)
    db.conversations.update({ "_id":conversation_id},{ "$push":{ "conversation_group": new_user}})
    return f"User {new_user} added to conversation {conversation_id}!"

#user("5f0c3f92ffc2be377870f314")

"""# Añade un usuario a un chat
@app.route ("/chat/<conversation_id>/adduser")
def user(conversation_id):
    conversation_id = ObjectId(conversation_id)
    new_user = ObjectId(request.args.get("user_id"))
    db.conversations.update({ "_id":conversation_id},{ "$push":{ "conversation_group": new_user}})
    return f"User {new_user} added to conversation {conversation_id}!"
"""

# Añade mesanjes a un chat

@app.route ("/chat/<conversation_id>/addmessage")
def createConv(conversation_id):
    conversation_id = ObjectId(conversation_id)
    participant = ObjectId(request.args.get("user_id"))
    text = request.args.get("text")
    conversation = {"chat_id":conversation_id, "user_id":participant, "text":text}
    db.messages.insert_one(conversation)
    return f"{text} said by participant: {participant} added to conversation {conversation_id}"



# Requests para sacar la lista de mesajes del chat elegido.
@app.route('/list/chats/<chat_id>')
def createListMessage(chat_name):
    '''
    Obtenemos los mensajes escritos en un unico chat
    '''

    coll_chat = db['conversations']
    list_message = coll_chat.find({'conversation_group': {'$eq': chat_name}})
    if list_message.count() == 0:
        raise NameError(f"Not found chat with id {chat_name}")
    else:
        coll_message = db['messages']
        allMessages = list(coll_message.find(
            {'chat': {'conversation_group': {'$eq': chat_name}}}, {'_id': 0, 'message': 1}))
        return allMessages



# Saca todos los mensajes de un chat

@app.route('/chat/message/<name>')
def getMessagesChat(name):

    query = {"chat_id":ObjectId(f"{name}")}
    mensajes = list(db.messages.find(query,{"_id":0}))
    #print(mensajes)
    return type(mensajes)

getMessagesChat("5f0c7695198fba6aebbe4e43")


"""@app.route('/chat/<conversation_id>/adduser') 
def insertUserChat(user,conversation):
    '''
    Crea un chat y añade usuarios 
    '''

    if len(list(db.users.find({"name": { "$eq": user } }))) > 0:
        pass
    else:
        error = f"No existe el usuario {user}"
        raise ValueError(error)
    user_id = list(db.users.find({"name": f"{user}"}))[0]['_id']
    conversation_id = list(db.conversations.find({"conversation_group": f"{conversation}"}))[0]['_id']
    update = db.conversations.update_one({ "_id":conversation_id},{ "$push":{ "participants": user_id}})
    return update"""

"""
@app.route('/chat/<conversation>/addusers/<participants>')    

def insertUsersChat(conversation,participants):
    '''
    Crea un chat y añade usuarios 
    '''

    for i in participants:
        print(i)
        if len(list(db.users.find({"name": { "$eq": f"{i}" } }))) > 0:
            pass
        else:
            error = f"No existe el usuario {i}"
            print(i)
            raise ValueError(error)
    
    name_IDS = []
    conversation_id = list(db.conversations.find({"conversation_group": f"{conversation}"}))[0]['_id']

    for i in participants:
        name_id = list(db.users.find({"name": f"{i}"}))[0]['_id']
        name_IDS.append(name_id)
  
    update = db.conversations.update_one({ "_id":conversation_id},{ "$push":{ "participants": name_IDS}})
    return update



"""



#Get all messages from a conversation



app.run("0.0.0.0", os.getenv("PORT"), debug=True)