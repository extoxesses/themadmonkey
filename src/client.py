
#!/usr/bin/env python
#
# Client used to bypass bot file size limit


from constants.config import Config
from constants.bot_constants import BotConstants
from utils.env_loader import EnvLoader

from client.downloaderClient import DownloaderClient

from pyrogram import Filters

import logging
logging.basicConfig(format=BotConstants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger("Client")


### --- Variables definitions

downloader = DownloaderClient()

pyroClient = EnvLoader.getClient()
pyroClient.run()


### --- Script

def allowedUser(message) :
  user = str(message.chat.username)
  return (user == Config.BOT_NAME)


def bypassMsg() :
  LOGGER.warn('Incoming message ignored!')


@pyroClient.on_message(~Filters.private)
def handler(client, msg) :
  if (not allowedUser(msg)) :
    username = str(msg.chat.username)
    LOGGER.warn('Request from invalid user! Requested username [' + username + ']')
    return

  if (not downloader.addMessage(msg)) :
    downloader.downloadFile(msg)


# Script entry point


