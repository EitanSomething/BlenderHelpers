import os

from rocketchat.api import RocketChatAPI
TOKEN = os.environ['TOKEN']
USERID = os.environ['USERID']

def login():
    global api
    api = RocketChatAPI(settings={'token': TOKEN, 'user_id': USERID,
                                  'domain': 'https://blender.chat'})
def sendMessage():
    with open('bugs_report.txt') as f:
        lines = f.readlines()
    message = ''.join(map(str,lines))
    api.send_message(message, "LpczsRCWtkYY6AzFt")
if __name__ == '__main__':
    login()
    sendMessage()
