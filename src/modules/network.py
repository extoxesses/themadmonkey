#!/usr/bin/env python
# Network services

import src.constants as CONSTS

import logging
import urllib

logging.basicConfig(format=CONSTS.LOGGER_FORMAT, level=logging.INFO)
logger = logging.getLogger(CONSTS.NETWORK_PACKAGE)

def whoYouAre(update, context):
  request = urllib.urlopen('https://ident.me')
  response = ''
  for line in request:
    response = response + line

  logger.info('Public ip: ' + response)
  context.message.reply_text('You are ' + response)
