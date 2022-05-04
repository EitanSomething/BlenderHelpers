import os

from rocketchat.api import RocketChatAPI
TOKEN = os.environ['TOKEN']
USERID = os.environ['USERID']

def login():
    global api
    api = RocketChatAPI(settings={'token': TOKEN, 'user_id': USERID,
                                  'domain': 'https://blender.chat'})
def sendMessage():
    api.send_message("@ThomasDinges Potential Spam. Not everything on the list is spam. https://github.com/EitanSomething/BlenderSpam/blob/auto_commits/logs.md","LpczsRCWtkYY6AzFt")
if __name__ == '__main__':
    login()
    sendMessage()