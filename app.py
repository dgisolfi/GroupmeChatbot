#Author: Daniel Gisolfi
#Date: 1/2/18
#GroupMe Chatbot
#v97

import os
import json
import random
import re
import sys

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


app = Flask(__name__)

bot = ChatBot("Marty",
	silence_performance_warning=True, 
	trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
	storage_adapter="chatterbot.storage.SQLStorageAdapter")

@app.route('/', methods=['POST'])

def webhook():
	data = request.get_json()

	if data['name'] != 'Marty':
		methodController(data)

	return "ok", 200


def methodController(data):
	text = data['text']
 
	originalWords = re.sub("[^\w]", " ",  data['text']).split()
	words = []

	greetings = [
		"Hello",
		"Hey",
		"Hi there",
		"Hi",
		"Hallo"
	]

	for word in originalWords:
		words.append(word.lower())

	if "marty" in words:
		if "echo" in words: 
			echo(data)
		# elif words in greetings:
		# 	greeting(data, greetings)
		else:
			converse(data)


def converse(data):

	bot.set_trainer(ListTrainer)
	bot.train(
		["Hello",
		"Hey",
		"How are you doing?",
		"I'm doing great."])

	bot.train(
		["what is your name?",
		"My name is Marty"])

	bot.train(
		["Who made you?",
		"Daniel Gisolfi"])

	# bot.train("chatterbot.corpus.english.conversations");
	# bot.train("chatterbot.corpus.english");
	
	userText = request.args.get(data['text'])
	msg = bot.get_response(userText)
	sendMessage(msg)

def greeting(data, greetings):
	name = re.sub("[^\w]", " ",  data['name']).split()
	firstName = name[0]

	x = random.randint(0,2)
	msg = greetings[x] + " " +  firstName
	sendMessage(msg)

def echo(data):
	msg = '{}, you sent "{}".'.format(data['name'], data['text'])
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
