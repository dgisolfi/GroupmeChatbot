#!/usr/bin/python3
# marty_bot.py
# 2018-07-29
# Purpose: Marty ChatBot
import os
import time
import json
import requests
from datetime import datetime
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Mark messages as read to avoid double sending
read_messages = []
filename = 'read_messages.txt'

api_host = 'http://138.68.140.175:5525'

bot_name = 'Marty'
bot_id = 'a6f23695345ae6009c7d8ccd4e'
group_id = 28081262
api_token = 'sSZSlKxXJyRd8SqFw5f8vikRNEiMZFWHgWWmCu7N'

#Create a instnce of a chatterbot and tell the bot where to find data
bot = ChatBot('Marty')
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train(
	"chatterbot.corpus.english.greetings",
	"data.marty"
)

def registerBot():
    #make a request to the api to register the bot
    try:
        requests.post(api_host +'/registerBot', 
        data=json.dumps({
            'bot_name': bot_name, 
            'bot_id': bot_id, 
            'group_id': group_id, 
            'api_token': api_token
            })
        )
    except:
        print('Failed to Register Bot with API.',
        'Are you sure the API address is correct?')

def getMessages():
    #make a request to the api for the most recent messages
    request = requests.get(api_host + '/requestMessages')
    lines = readMsgIDs()
  
    if request.status_code == 200:
        # try:
        messages = request.json()['data']['response']['messages']
        # except:
        #     print('no messages')
        #     return None
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
        for line in lines:
            line.replace("\n", "")
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
            file.write(str(read_messages[count] + '\n'))
            count += 1

    file.close()
   

def main():
    print('Starting bot loop')
    # registerBot()
    while True:
        try:
            user_msgs = []
            user_msgs.append(getMessages())
            if len(user_msgs):
                print(len(user_msgs))
                for msg in user_msgs:
                    # sendMessage(martyResponse(msg))
                    continue
            writeMsgIDs('write')
            time.sleep(3)
        except KeyboardInterrupt:
            break
    

if __name__ == '__main__':
    main()
