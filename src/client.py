
#!/usr/bin/env python
#
# Client used to bypass bot file size limit


from constants.bot_constants import BotConstants
from constants.config import Config
from utils.env_loader import EnvLoader
from client.downloaderClient import DownloaderClient

from pyrogram import Filters

import sys

import logging
logging.basicConfig(format=BotConstants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger("Client")


# --- Script function

config = None

def getEnvPath() :
  path = str(sys.argv[1])
  LOGGER.info('Environment .env file path: ' + path)
  return path
  
def allowedUser(message) :
  user = str(message.chat.username)
  return (user == config.BOT_NAME)

def bypassMsg() :
  LOGGER.warn('Incoming message ignored!')



# --- Script entry point

if (len(sys.argv) != 2) :
  LOGGER.error('Invalid number of parameter: .env file is required!')
  sys.exit()

env_path = getEnvPath()
config = Config(env_path)

downloader = DownloaderClient()

pyroClient = EnvLoader.getClient(config)


@pyroClient.on_message(~Filters.private)
def handler(client, msg) :
  if (not allowedUser(msg)) :
    username = str(msg.chat.username)
    LOGGER.warn('Request from invalid user! Requested username [' + username + ']')
    return

  if (not downloader.addMessage(msg)) :
    downloader.downloadFile(msg)


pyroClient.run()
