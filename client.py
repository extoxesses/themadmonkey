
#!/usr/bin/env python
# Client used to bypass bot file size limit

import resources.reserved as RESERVED
from resources.reserved import pyroClient
import src.constants as CONSTS

from src.client.downloaderClient import DownloaderClient

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
  text = str(msg.text)

  if (not allowedUser(msg)) :
    LOGGER.info('Request from invalid user, or this is an outcoming message!')
    return
  

  print(msg)

  if (RESERVED.REF_MSG in str(text).lower()) :
    downloader.setReceived()
    LOGGER.info('Received forward file control message...')
    return

  if (downloader.isForwarded()) :
    LOGGER.info('Downloading incoming message...')
    downloader.download(msg)
    return

  bypassMsg()



pyroClient.run()
