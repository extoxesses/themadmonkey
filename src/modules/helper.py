#!/usr/bin/env python
# Help endpoints


# Projects imports
import src.constants as CONSTS
import resources.reserved as RESERVED

# Default imports
import logging
import os

logging.basicConfig(format=CONSTS.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(CONSTS.HELP_PACKAGE)


def hi(bot, context):
  user_id = context['message']['chat']['id']
  try:
    user_tag = RESERVED.VALID_USERS[user_id]
    context.message.reply_text('Hi, ' + user_tag + '!')
  except KeyError as e:
    context.message.reply_text('Who are you?')


def errorHandler(bot, context, error) :
  LOGGER.error(error)
