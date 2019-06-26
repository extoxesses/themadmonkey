#!/usr/bin/env python

#  _   _                                _                         _              
# | | | |                              | |                       | |             
# | |_| |__   ___   _ __ ___   __ _  __| |  _ __ ___   ___  _ __ | | __ ___ _   _ 
# | __| '_ \ / _ \ | '_ ` _ \ / _` |/ _` | | '_ ` _ \ / _ \| '_ \| |/ // _ \ | | |
# | |_| | | |  __/ | | | | | | (_| | (_| | | | | | | | (_) | | | |   <|  __/ |_| |
#  \__|_| |_|\___| |_| |_| |_|\__,_|\__,_| |_| |_| |_|\___/|_| |_|_|\_\\___|\__, |
#                                                                           __/ |
#                                                                          |___/ 
# A simple telegram bot for network analysis...


from modules.helper import Helper
from modules.msgmanager import MessageManagerService
from modules.network import NetworkService
from constants.bot_constants import BotConstants
from constants.config import Config

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import os

import logging
logging.basicConfig(format=BotConstants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(BotConstants.MAIN)



def getUpdater():
  LOGGER.info('Begin bot configuration...')
  bot = Updater(Config.TOKEN)
  dp = bot.dispatcher

  dp.add_handler(CommandHandler("hi", Helper.hi))
  dp.add_handler(CommandHandler("whoyouare", NetworkService.whoYouAre))

  dp.add_handler(MessageHandler(Filters.text, MessageManagerService.txtMsgHandler))
  dp.add_handler(MessageHandler(Filters.document, MessageManagerService.docAttachHandler))

  # log all errors
  dp.add_error_handler(Helper.errorHandler)

  LOGGER.info('Bot configuration completed!')
  return bot



def main():
  # Start bot
  LOGGER.info('Bot started...')
  updater = getUpdater()

  LOGGER.info('Listener started...')
  updater.start_polling()
  updater.idle()



if __name__ == '__main__':
    main()
