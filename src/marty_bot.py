#!/usr/bin/python3
# marty_bot.py
# 2018-07-29
# Purpose: Marty ChatBot
import os
import time
import json
import pickle
import requests
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Mark messages as read to avoid double sending
read_messages = []
filename = 'read_messages.txt'

api_host = None

bot_name = 'Marty'
bot_id = None
group_id = None
api_token = None

#Create a instnce of a chatterbot and tell the bot where to find data
bot = ChatBot('Marty')
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train(
	"chatterbot.corpus.english.greetings",
	"data.marty"
)

def registerBot():
    #make a request to the api to register the bot
    requests.post(api_host +'/registerBot', 
    data=json.dumps({
        'bot_name': bot_name, 
        'bot_id': bot_id, 
        'group_id': group_id, 
        'api_token': api_token
        })
    )

def getMessages():
    #make a request to the api for the most recent messages
    request = requests.get(api_host + '/requestMessages')
    lines = readMsgIDs()

    if (request.status_code == 200):
        messages = request.json()['data']['response']['messages']
        for message in messages:
            #Check Marty sent the message
            if message['name'] == 'Marty':
                continue
            #Check if Marty was called in the message
            elif 'marty' in message['text'].lower():
                message['text'].replace("marty", "")
                
                if str(message['id']) in lines:
                    continue
                else:
                    read_messages.append(message['id'])
                    return message['text']
            else:
                return None


def sendMessage(msg):
    send_status = requests.post(
        api_host + '/sendMsg',
        data=json.dumps({'msg': str(msg)}))
    print(send_status, msg)

def martyResponse(msg):
	response = bot.get_response(msg)
	return response

def readMsgIDs():
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        print(lines)
        file.close()        
        return lines
    except:
        writeMsgIDs('initilize')
        print('File not found or cannot be read')
   
def writeMsgIDs(arg):
    try:
        file = open(filename, 'a+')
    except:
        print('File cannot be written')
    if arg == 'initilize':
        file.write('000000')
    else:
        count = 0
        for id in read_messages:
            file.write(str(read_messages[count]))
            count += 1

    file.close()
   

def main():
    print('Starting bot loop')
    # registerBot()
    while True:
        try:
            user_msgs = []
            user_msgs.append(getMessages())
            print(len(user_msgs))
            if len(user_msgs):
                for msg in user_msgs:
                    # sendMessage(martyResponse(msg))
                    continue
            writeMsgIDs('write')
            time.sleep(3)
        except KeyboardInterrupt:
            break
    

if __name__ == '__main__':
    main()
