#!/usr/bin/env python
#
# Help endpoints


from constants.bot_constants import BotConstants

from os import environ

import logging
logging.basicConfig(format=BotConstants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(BotConstants.HELP_PACKAGE)


config = None

class Helper :

  def hi(bot, context):
    user_id = context['message']['chat']['id']
    if ((config != None) and (str(user_id) == str(config.OWNER_ID))):
      context.message.reply_text('Hi, ' + config.OWNER_NAME + '!')

    else:
      context.message.reply_text('Who are you?')


  def errorHandler(bot, context, error) :
    LOGGER.error(error)
