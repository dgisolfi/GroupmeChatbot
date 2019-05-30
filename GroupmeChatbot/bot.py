#!/usr/bin/python3
# 2019-05-29

import re
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Bot:
    def __init__(self, name, bot_id, group_id, api_token):
        self.name = name
        self.bot_id = bot_id
        self.group_id = group_id
        self.api_token = api_token
        self.api_base_url = 'https://api.groupme.com/v3'
        self.api_session = requests.session()

        # Create a instnce of a chatterbot and tell the bot where to find data
        self.chatbot = ChatBot(self.name)
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train(
            'chatterbot.corpus.english'
        )

    def sendMessage(self, msg):
        '''Send a message from the bot to its assigned group.
            Args:
                msg (str): message to be sent to group
            Returns:
                request response
        '''
        # set parameters for post request
        params = {
            'bot_id': self.bot_id,
            'text': msg
        }
        # send the request to the api and get the results in the response var
        response = self.api_session.post(
            f'{self.api_base_url}/bots/post', 
            params=params
        )
        return response
        
    def getMessages(self):
        '''Get all messages for the bot's group chat.
            Args:
                none
            Returns:
                request response
        '''
        # authenticate the request with the api token
        params = {
            'token': self.api_token
        }
        # get the messages for the bot's group
        response = self.api_session.post(
            f'{self.api_base_url}/groups/{self.group_id}/messages', 
            params=params
        )
        return response

    def checkForMention(self, msg):
        '''Checks the recent messages of the bots group for instances of its name
            Args:
                msg (str): message sent in group chat
            Returns:
                boolean: a value denoting if the bot was mentioned or not
        '''
        return re.match(r'.*@'+self.name+r'.*', msg)

    def removeMention(self, msg):
        '''Checks the recent messages of the bots group for instances of its name
            Args:
                msg (str): message sent in group chat
            Returns:
                msg (str): a messaged with the '@<bot_name>' removed
        '''
        return re.sub(f'@{self.name}', '', msg)
        
    def getResponse(self, msg):
        '''Given a message the appropriate response is returned.
            Args:
                msg (str): a message to respond to
            Returns:
                response (str): the bot's response to the message
        '''
        # makes a call to the chatterbot package for a response
        response = self.chatbot.get_response(msg)
        return response