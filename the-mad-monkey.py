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

import sys
sys.path.append('resources/')
sys.path.append('src/')
sys.path.append('src/modules')

import constants, reserved, helper, network, textmanager

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format=constants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(constants.MAIN)




def testhandler(bot, update):
  print (update.message.document.file_id)
  # file = bot.getFile(update.message.voice.file_id)
  # print (file)
  # print ("file_id: " + str(update.message.voice.file_id))
  # file.download('voice.ogg')



def getUpdater():
  LOGGER.info('Begin bot configuration...')
  bot = Updater(reserved.TMM_TOKEN)

  # Get the dispatcher to register handlers
  dp = bot.dispatcher

  # on different commands - answer in Telegram
  dp.add_handler(CommandHandler("hi", helper.hi))
  dp.add_handler(CommandHandler("whoyouare", network.whoYouAre))

  # on noncommand i.e message - echo the message on Telegram
  textManager = textmanager.TextManager(bot)
  dp.add_handler(MessageHandler(Filters.text, textManager.manageText))
  dp.add_handler(MessageHandler(Filters.document, testhandler))

  # log all errors
  # dp.add_error_handler(error)

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
