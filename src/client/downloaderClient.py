
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
    self.success_reply = "Downloads completed successfully!"
    self.error_reply = "An error occurred while downloading files. Checks logs for additional informations."
    self.total_docs_size = 0


  def addMessage(self, msg) :
    if (msg.media) :
      file_name = msg.document.file_name

      self.medias[file_name] = msg
      LOGGER.info('Added new message to the dictionary with id: ' + file_name)
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
    if (percentage >= 100) :
      super.dropAll()


  def downloadFile(self, request) :
    req_msg = str(request.text)
    if (req_msg == None) :
      return

    if (CONSTS.FILE_ERROR_FORWARD_MSG not in req_msg) :
      return

    file_name = req_msg.split(':')[1].lstrip()
    LOGGER.info('Request to download file: ' + file_name)

    message = self.medias.get(file_name)
    if (message == None) :
      LOGGER.warn("Required message does not exists!")
      return

    try :
      LOGGER.info('Starting download attempt...')
      self.total_docs_size = message.document.file_size
      path = message.download(progress=self.progressCallback)
      LOGGER.info('File downloaded at: ' + path)
      message.reply(self.success_reply)
      del self.medias[file_name]

    except :
      message.reply(self.error_reply)
