#Author: Daniel Gisolfi
#Date: 8/4/17
#GroupMe Chatbot
#Version 69
  
import os
import sys
import json
import random
import re
import json
  
  
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
  
from chatterbot.trainers import ChatterBotCorpusTrainer
  
app = Flask(__name__)
  
@app.route('/', methods=['POST'])
  
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  methodController(data)
  return "ok", 200
  
def sendMessage(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  
  data = {
        'bot_id' : os.getenv('GROUPME_BOT_ID'),
        'text'   : msg,
       }
  
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
  
def methodController(data):
  
  # name = re.sub("[^\w]", " ",  data['name']).split()
  # firstName = name[0]
  text = data['text']
 
  originalWords = re.sub("[^\w]", " ",  data['text']).split()
  words = []
  
  for word in originalWords:
    words.append(word.lower())
  if "marty" in words:
    if "quote" in words:
      quote()
    elif "rules" in words:
      rules()
    elif "echo" in words: 
      echo(data)
    else:
      converse(data)
    # elif "derivative" in words:
    #   x = int(re.search(r'\d+', text).group())  
    #   derivative(x)
    # elif data['name'] != "Marty":
    #   sendMessage("Starting converse function...")
    #   converse(data)
  
    
    
  
def converse(data):
  
  bot = ChatBot("Marty",silence_performance_warning=True)
  # bot.set_trainer(ChatterBotCorpusTrainer)
  
  conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "My name is Marty."
  ]
  
  bot.set_trainer(ListTrainer)
  bot.train(conversation)
  bot.train('chatterbot.corpus.english')
  
  msg = bot.get_response(data['text'])
  sendMessage(msg)
  
def echo(data):
  if data['name'] != 'Marty':
    msg = data['text']
    sendMessage(msg)
  
def quote():
  if data['name'] != 'Marty':
    msg = "quote"
    sendMessage(msg)
  
def notification():
  pass
  
def rules():
  rules = [
  "1: Nothing bad can ever happen\n",
  "2: The three best words free, food, stuff\n",
  "3: Any money is good money\n",
  "4: When you have a choice between drinking and not drinking always pick drinking\n",
  "5: Make sure you can swipe\n",
  "6: Don't forget your keys\n",
  "7: Stop drinking random drinks you find in the bar\n",
  "8: Don't stick your dick in crazy (handies are A-OK)\n",
  "9: Any girl with un naturally died hair is at least a little crazy\n",
  "10: Know where you're pissing (or puking)\n",
  "11: Never pay more than $3 for a cab or $5 for a party\n",
  "12: Fuck joe the RD (foy)\n",
  "13: Love is a light switch away(jack)\n",
  "14: Never chuck(luke and jack)\n",
  "15: Don't talk to your RA when you're drunk (Brendan)\n",
  "16: $3 in the shirt pocket\n",
  "17: No rules apply while in the bush\n",
  "18: All card games should involve at least a little bullying\n",
  "19: Rules are made to be broken\n"]
 
  for x in rules:
    ruleList = ''.join(rules)
  sendMessage(ruleList)
 
 
def f(x):
  return x**2
 
def derivative(x):
  h = 1./1000.
  rise = f(x+h) - f(x)
  run = h
  slope = rise/run
  sendMessage("The derivative of " + str(x) + " is " + str(slope))
 
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
