from textblob import TextBlob
from bson.objectid import ObjectId
from flask import Flask, request
from pymongo import MongoClient

client = MongoClient()
db = client.get_database("My-Super-API")

def formatendadoChats(chat_id):
    '''
    Analizamos los sentimientos de los mensajes escritos en un grupo
    '''

    tup = []
    coll_message = db['messages']
    allMessages = list(coll_message.find(
        {'chat': {"$eq": ObjectId(chat_id)}}, {'_id': 0, 'message': 1}))
    for i in allMessages:
        for _, v in i.items():
            tup.append(v)
    frase = ' '.join(tuple(tup))
    en_blob = TextBlob(frase)
    en_blob = en_blob.translate(from_lang='es', to='en')
    return en_blob.sentiment


def formatendadoUsers(user_id):
    '''
    Analizamos los sentimientos de los mensajes escritos por un usuario
    '''

    tup1 = []
    coll_message = db['messages']
    mensajesUsuario = list(coll_message.find(
        {'user': {"$eq": ObjectId(user_id)}}, {'_id': 0, 'message': 1}))
    for i in mensajesUsuario:
        for _, v in i.items():
            tup1.append(v)
    frase = ' '.join(tuple(tup1))
    en_blob = TextBlob(frase)
    en_blob = en_blob.translate(from_lang='es', to='en')
    return en_blob.sentiment