#Author: Daniel Gisolfi
#Date: 3/15/18
#Neep Peep script

import os
import json
import random
import re
import sys

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

import time, random, datetime

neepPeep()

app = Flask(__name__)

@app.route('/', methods=['POST'])

def webhook():
	data = request.get_json()
	print("webhook sarted")
	return "ok", 200

def neepPeep():
	#create  loop
	while True:
		#uses the dayCheck function to get the right message else a random one.
		msg = "Neep Peep"
		sendMessage(msg)
		print("sent message")
		#create a random interval of time between 1 - 8 hours
		# waitTime = randint(10800,43200)
		waitTime = (5)
		print(waitTime/60/60)
		i = 0s
		while i < waitTime:
		    progress(i, waitTime, status='waiting to send next message')
		    time.sleep(0.5)  # emulating long-playing job
		    i += 1
		#print aprox how many hours the function will sleep

		#set the fucntion to sleep for x amount of time then run again, and loop
		print("Start : %s" % time.ctime())
		# print("Start")
		time.sleep(waitTime)
		# print("End")
		print("End : %s" % time.ctime())


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



