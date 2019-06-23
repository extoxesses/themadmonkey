
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
    self.reply = "" # TODO: Defile this message
    self.error_reply = "" # TODO: Defile this message

  def addMessage(self, msg) :
    if (msg.media) :
      # msg_id = str(msg.message_id)
      msg_id = msg.document.file_name

      self.medias[msg_id] = msg
      LOGGER.info('Added new message to the dictionary with id: ' + msg_id)
      return True

    return False



  def dropThat(self, delta) :
    # TODO: this method should remove all entries that are older than the given 'delta'
    LOGGER.info('Method not yet implemented!')


  def progressCallback(client, current, total, *args) :
    print(client)
    print(current)
    print(total)
    # LOGGER.info('File ' + client + ' status: [' + current + '/' + total + ']')


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
      path = message.download(progress=self.progressCallback)
      LOGGER.info('File downloaded at: ' + path)
      message.reply(self.reply)
      del self.medias[msg_id]
    except :
      message.reply(self.error_reply)
