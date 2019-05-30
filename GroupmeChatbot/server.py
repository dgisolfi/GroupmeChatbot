#!/usr/bin/python3

import os
import markdown
from GroupmeChatbot.bot import Bot
from flask import Flask, request

# Create instance of flask
server = Flask(__name__)
server.config['JSON_SORT_KEYS'] = False


name = os.getenv('BOT_NAME', None)
bot_id = os.getenv('BOT_ID', None)
group_id = os.getenv('GROUP_ID', None)
api_token = os.getenv('API_TOKEN', None)

# setup bot
bot = Bot(name, bot_id, group_id, api_token)

@server.route('/', methods=['GET'])
def index():
    try:
        markdown_file = open('README.md', 'r')
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content), 200
    except:
        return 'Project Documentation Not found', 404
        
@server.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if data is not None:
        if bot.checkForMention(data['text']):
            msg = bot.removeMention(data['text'])
            response = bot.getResponse(msg)
            bot.sendMessage(response)
        
        return 'OK', 200
    return 'No Message Provided', 404
    