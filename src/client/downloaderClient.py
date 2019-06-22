
#!/usr/bin/env python
# Class used from download client

import sys

import src.constants as CONSTS

import logging
logging.basicConfig(format=CONSTS.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger("DownloaderClient")


class DownloaderClient :

  def __init__(self):
    self.forwarded = False
    self.correctMsg = ""
    self.errorMsg = ""

  def setReceived(self) :
    self.forwarded = True

  def unload(self) :
    self.forwarded = False

  def downloadFile(self, msg) :
    try :
      msg.downlod()
      msg.reply(self.correctMsg)
    except :
      LOGGER.error("An error was raised during the file download phase - ", sys.exc_info()[0])
      msg.reply(self.errorMsg)

    self.forwarded = False


  def isForwarded(self) :
    return self.forwarded