#Author: Daniel Gisolfi
#Date: 1/2/18
#GroupMe Chatbot
#Version 71

import os
import json
import random
import re

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
	data = request.get_json()

	if data['name'] != 'Marty':
		methodController(data)
		send_message(msg)

	return "ok", 200


def methodController(data):
	text = data['text']
 
	originalWords = re.sub("[^\w]", " ",  data['text']).split()
	words = []
	
	for word in originalWords:
		words.append(word.lower())
	if "hello" or "hi" or "hey" in words:
		converse(data)


def converse(data):
	responese = [
		"Hello",
		"Hey",
		"Hi there"
	]

	x = random.randint(0,2)
	msg = responese[x] 
	sendMessage(msg)


def sendMessage(msg):
	url  = 'https://api.groupme.com/v3/bots/post'

	data = {
		'bot_id' : os.getenv('GROUPME_BOT_ID'),
		'text'   : msg,
		}
		
	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()

def log(msg):
	print(str(msg))
	sys.stdout.flush()
