# Chat-Sentiment-Analysis-Project

![alt imagen](Input/Chat-Analysis.jpeg)

## Project Goals

- Write an API in `flask` just to store chat messages in a mongodb database.
- Extract sentiment from chat messages and perform a report over a whole conversation
- Recommend friends to a user based on the contents from chat `documents` using a recommender system with `NLP` analysis



## Overview 🚀

Detailed analysis of how it works can be found in the file 'main.ipynb'.

El resto de carpetas siguen la denominación estándar para el tipo de datos que poseen,y no requieren aclaraciones adicionales.

Program execution: 'path / python3 main.py' 🔧

Program  Execution in Jupyter Notebook: 'path / jupyter-notebook Demo.py'


## Basic Operations


Add user - /user/create/ - (Ej: "http://0.0.0.0:4500/user/create/Paula")

Create Chat - /chat/create - (Ej: "http://0.0.0.0:4500/chat/create/Work")

Add users to a chat - /chat/<chat_id>/adduser - (Ej: "http://0.0.0.0:4500/chat/0/adduser?username=Laura")

Add messages to a chat - /chat/<chat_id>/addmessage - (Ej: "http://0.0.0.0:4500/chat/0/addmessage?username=Juan")

