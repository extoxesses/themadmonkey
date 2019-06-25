
#!/usr/bin/env python
#
# Client used to bypass bot file size limit

import resources.reserved as RESERVED
from resources.reserved import pyroClient
import constants as CONSTS

from client.downloaderClient import DownloaderClient

from pyrogram import Filters

import logging
logging.basicConfig(format=CONSTS.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger("Client")

downloader = DownloaderClient()

### --- Script

def allowedUser(message) :
  user = str(message.chat.username)
  return (user == RESERVED.BOT_NAME)


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


pyroClient.run()
