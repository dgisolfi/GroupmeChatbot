# GroupmeChatbot [![GroupmeChatbot version](https://img.shields.io/pypi/v/GroupmeChatbot.svg)](https://pypi.org/project/GroupmeChatbot)

A Bot that responds with custom messages when mentioned in a Groupme chat

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Groupme Bot?

 A GroupMe bot can be created [here](https://dev.groupme.com/bots) and using the Groupme API can send messages to its assigned group. This particular bot uses a callback URL to be notified of new messages. Once notified the message will be parsed and a response will be created if the bot was specifically mentioned by name example: `@marty how are you?`. 

## Usage

Once a bot is registered with Groupme the following requirements must be specified in the form of environment variables:

* **BOT_NAME** - Is the name of the bot that members of the group chat can refer to it by.

  Example: `BOT_NAME=marty`    
  
* **BOT_ID** - The assigned bot ID by GroupMe.

  Example: `BOT_ID=a6a7a7a7a7a7a7a7a77a7a7`    

* **GROUP_ID** - The ID of the Groupme Chat where the bot resides

  Example: `GROUP_ID=0987890987`    
* **API_TOKEN** - The api token for the authorized Groupme account

  Example: `API_TOKEN=983u4ritgo0v98ujkorf`

After the environment variables have been set run the Flask server, `python -m GroupmeChatbot`

## Customization/Additions

Feature Additions/Suggestions are welcome, for any particular functionality that may need to be added for a particular use case, simple parse the incoming messages looking for specified input in the `server.py` file and add methods in the bot class to perform the desired function.


