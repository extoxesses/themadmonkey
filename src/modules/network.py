#!/usr/bin/env python
#
# Network services


from constants.bot_constants import BotConstants

import urllib

import logging
logging.basicConfig(format=BotConstants.LOGGER_FORMAT, level=logging.INFO)
logger = logging.getLogger(BotConstants.NETWORK_PACKAGE)



class NetworkService :
  
  def whoYouAre(update, context):
    request = urllib.urlopen('https://ident.me')
    response = ''
    for line in request:
      response = response + line

    logger.info('Public ip: ' + response)
    context.message.reply_text('You are ' + response)
