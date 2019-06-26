#!/usr/bin/env python
#
# Bot constants

from os import environ



class BotConstants :

  # Default logger format
  LOGGER_FORMAT = '[%(asctime)s] %(levelname)s\t%(name)s\t%(message)s'

  # Modules names
  MAIN = 'main'
  CUSTOM_PACKAGE = 'custom'
  HELP_PACKAGE = 'helper'
  MSG_PACKAGE = 'messages'
  NETWORK_PACKAGE = 'network'
  USERS_PACKAGE = 'users'

  # Paths - TODO check behaviours under docker
  DOWNLOAD_PATH = environ['HOME'] + '/the-mad-monkey/'

  # Bot-client sync message
  FILE_ERROR_FORWARD_MSG = '⚠️ File too big! Trying to download it using the client. File name: '
