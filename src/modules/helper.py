#!/usr/bin/env python
#
# Help endpoints


from constants.bot_constants import BotConstants

from os import environ

import logging
logging.basicConfig(format=BotConstants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(BotConstants.HELP_PACKAGE)



class Helper :

  def hi(bot, context):
    user_id = context['message']['chat']['id']
    try:
      user_tag = RESERVED.VALID_USERS[user_id]
      context.message.reply_text('Hi, ' + user_tag + '!')
    except KeyError as e:
      context.message.reply_text('Who are you?')


  def errorHandler(bot, context, error) :
    LOGGER.error(error)
