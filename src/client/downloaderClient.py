
#!/usr/bin/env python
# Class used from download client

import sys

import src.constants as CONSTS

import logging
logging.basicConfig(format=CONSTS.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger("DownloaderClient")


class DownloaderClient :

  def __init__(self):
    self.medias = {}
    self.reply = "REPLY"       # TODO
    self.error_reply = "ERROR" # TODO
    self.total_docs_size = 0


  def addMessage(self, msg) :
    if (msg.media) :
      # msg_id = str(msg.message_id)
      msg_id = msg.document.file_name

      self.medias[msg_id] = msg
      LOGGER.info('Added new message to the dictionary with id: ' + msg_id)
      return True

    return False


  def getTotalMsgSize(self) :
    return self.total_docs_size


  def dropAll(self, delta) :
    LOGGER.info('Dropping all cached files...')
    total_docs_size = 0
    self.medias = {}

    print(self.medias)


  def progressCallback(client, current, total, *args) :
    percentage = float(total) / float(client.getTotalMsgSize())
    percString = '%.3f'%(percentage)
    LOGGER.info("Progress: " + percString + " %")
    if (percentage == 100) :
      super.dropAll()


  def downloadFile(self, request) :
    req_msg = str(request.text)
    if (req_msg == None) :
      return

    msg_id = req_msg.split(':')[1].lstrip()
    LOGGER.info('Request to download file: ' + msg_id)

    message = self.medias.get(msg_id)
    if (message == None) :
      LOGGER.warn("Required message does not exists!")
      return

    try :
      LOGGER.info('Starting download attempt...')
      self.total_docs_size = message.document.file_size
      path = message.download(progress=self.progressCallback)
      LOGGER.info('File downloaded at: ' + path)
      message.reply(self.reply)
      del self.medias[msg_id]

    except :
      message.reply(self.error_reply)
