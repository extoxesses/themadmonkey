#!/usr/bin/env python
# Endpoints for non-command messages management

import src.constants
import src.utils.usersutils
import resources.reserved

import os
import logging

logging.basicConfig(format=src.constants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(src.constants.MAIN)


def txtMsgHandler(update, context):
  print (context.message.chat.id)
  context.message.reply_text(context.message.text)


def docAttachHandler(bot, context):
  user = context.message.chat
  if not src.utils.usersutils.checkUser(user, resources.reserved.VALID_USERS) :
    LOGGER.warn ('Invalid request form: ' + user.first_name)
    context.message.reply_text('Hi ' + user.first_name + '! You are not allowed to upload file on this server!')
    return
  
  doc = context.message.document
  file = bot.getFile(doc.file_id)
  LOGGER.info ('Receive file: ' + doc.file_name)

  home = src.constants.DOWNLOAD_PATH + doc.file_name
  file.download(home) # TODO fix this path
