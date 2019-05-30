#!/usr/bin/python3
# 2019-05-30

from GroupmeChatbot import Bot
import pytest
import json
import os

class TestGroupMeBot:
    name = os.getenv('BOT_NAME', None)
    bot_id = os.getenv('BOT_ID', None)
    group_id = os.getenv('GROUP_ID', None)
    api_token = os.getenv('API_TOKEN', None)

    # make instance of bot
    bot = Bot(name, bot_id, group_id, api_token)

    def testSendMessage(self):
        response = self.bot.sendMessage('test')
        # check for success
        assert response.status_code is 200

    def testGetMessages(self):
        response = self.bot.getMessages()
        # check for success
        assert response.status_code is 200
        # There should be a dictionary of messages returned
        assert response.json() is not None

    def testForMention(self):
        mention_msg = f'@{self.name} hi'
        msg = 'hi'

        assert self.bot.checkForMention(mention_msg) is True
        assert self.bot.checkForMention(msg) is False

    def testRemoveMention(self):
        mention_msg = f'@{self.name} hi'
        assert self.bot.removeMention(mention_msg) == 'hi'

    def testGetResponse(self):
        msg = 'hi'
        response = self.bot.getResponse(msg)
        assert response != ''