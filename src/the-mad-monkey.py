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
import constants
import resources.reserved
import modules.helper
import modules.network
import modules.msgmanager as MSG_MANAGER

# Default imports
import logging
import os

# Third parties import
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format=constants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(constants.MAIN)



def getUpdater():
  LOGGER.info('Begin bot configuration...')
  bot = Updater(resources.reserved.TMM_TOKEN)

  # Get the dispatcher to register handlers
  dp = bot.dispatcher

  # on different commands - answer in Telegram
  dp.add_handler(CommandHandler("hi", modules.helper.hi))
  dp.add_handler(CommandHandler("whoyouare", modules.network.whoYouAre))

  # on noncommand i.e message - echo the message on Telegram
  dp.add_handler(MessageHandler(Filters.text, MSG_MANAGER.txtMsgHandler))
  # dp.add_handler(MessageHandler(Filters.video, MSG_MANAGER.videoHandler))
  dp.add_handler(MessageHandler(Filters.document, MSG_MANAGER.docAttachHandler))

  # log all errors
  dp.add_error_handler(modules.helper.errorHandler)

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
