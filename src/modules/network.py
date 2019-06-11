#!/usr/bin/env python
# Network services

import src.constants

import logging
import urllib

logging.basicConfig(format=src.constants.LOGGER_FORMAT, level=logging.INFO)
logger = logging.getLogger(src.constants.NETWORK_PACKAGE)

def whoYouAre(update, context):
  request = urllib.urlopen('https://ident.me')
  response = ''
  for line in request:
    response = response + line

  logger.info('Public ip: ' + response)
  context.message.reply_text('You are ' + response)
