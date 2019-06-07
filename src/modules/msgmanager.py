#!/usr/bin/env python
# Endpoints for non-command messages management

import sys
sys.path.append('src/')

import constants

import os
import logging

logging.basicConfig(format=constants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(constants.MAIN)


def txtMsgHandler(update, context):
  context.message.reply_text(context.message.text)


def docAttachHandler(bot, update):
  doc = update.message.document
  file = bot.getFile(doc.file_id)
  LOGGER.info ('Receive file: ' + doc.file_name)

  home = os.environ['HOME'] + '/' + doc.file_name
  file.download(home) # TODO fix this path
