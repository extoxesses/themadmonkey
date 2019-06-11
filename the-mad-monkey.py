#!/usr/bin/env python

#  _   _                                _                         _              
# | | | |                              | |                       | |             
# | |_| |__   ___   _ __ ___   __ _  __| |  _ __ ___   ___  _ __ | | _____ _   _ 
# | __| '_ \ / _ \ | '_ ` _ \ / _` |/ _` | | '_ ` _ \ / _ \| '_ \| |/ / _ \ | | |
# | |_| | | |  __/ | | | | | | (_| | (_| | | | | | | | (_) | | | |   <  __/ |_| |
#  \__|_| |_|\___| |_| |_| |_|\__,_|\__,_| |_| |_| |_|\___/|_| |_|_|\_\___|\__, |
#                                                                           __/ |
#                                                                          |___/ 
# A simple telegram bot for network analysis...

# Project imports
import src.constants
import resources.reserved
import src.modules.helper
import src.modules.network
import src.modules.msgmanager

# Default imports
import logging
import os

# Third parties import
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format=src.constants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(src.constants.MAIN)



def getUpdater():
  LOGGER.info('Begin bot configuration...')
  bot = Updater(resources.reserved.TMM_TOKEN)

  # Get the dispatcher to register handlers
  dp = bot.dispatcher

  # on different commands - answer in Telegram
  dp.add_handler(CommandHandler("hi", src.modules.helper.hi))
  dp.add_handler(CommandHandler("whoyouare", src.modules.network.whoYouAre))

  # on noncommand i.e message - echo the message on Telegram
  dp.add_handler(MessageHandler(Filters.text, src.modules.msgmanager.txtMsgHandler))
  dp.add_handler(MessageHandler(Filters.document, src.modules.msgmanager.docAttachHandler))

  # log all errors
  dp.add_error_handler(src.modules.helper.errorHandler)

  LOGGER.info('configuration completed!')
  return bot



def main():
  LOGGER.info('Bot started...')
  # Build updater object
  updater = getUpdater()

  # Start the Bot
  LOGGER.info('Listener started...')
  updater.start_polling()
  updater.idle()



if __name__ == '__main__':
    main()
