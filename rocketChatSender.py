from rocketchat.api import RocketChatAPI
 
import os
TOKEN = os.environ.get("TOKEN")
USERID = os.environ.get("USERID")
def sendSpam():
  rocket = RocketChatBase

