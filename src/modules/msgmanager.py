#!/usr/bin/env python
# Endpoints for non-command messages management

import src.constants as CONSTS
import resources.reserved as RESERVED

import os
import logging

logging.basicConfig(format=CONSTS.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(CONSTS.MSG_PACKAGE)


def txtMsgHandler(update, context) :
  LOGGER.info('Message from ' + str(context.message.chat.id))
  context.message.reply_text(context.message.text)


def docAttachHandler(bot, context) :
  try:
    user = context.message.chat
    if not src.utils.usersutils.checkUser(user, RESERVED.VALID_USERS) :
      LOGGER.warn('Invalid request form user ' + user.first_name)
      context.message.reply_text('Hi ' + user.first_name + '! You are not allowed to upload file on this server!')
      return
    
    doc = context.message.document
    file = bot.getFile(doc.file_id)
    LOGGER.info ('Receive file: ' + doc.file_name)

    home = CONSTS.DOWNLOAD_PATH + doc.file_name
    file.download(home)
  
  except:
    file_name = str(context.message.document.file_name)
    recipient_id = str(context.message.chat.id)
    
    LOGGER.info(CONSTS.FORWARD_MSG + file_name)
    context.message.reply_text(CONSTS.FORWARD_MSG + file_name)
