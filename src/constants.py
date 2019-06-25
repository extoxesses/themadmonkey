#!/usr/bin/env python
# Bot constants

import os

LOGGER_FORMAT = '[%(asctime)s] %(levelname)s\t%(name)s\t%(message)s'

MAIN = 'main'
CUSTOM_PACKAGE = 'custom'
HELP_PACKAGE = 'helper'
MSG_PACKAGE = 'messages'
NETWORK_PACKAGE = 'network'
USERS_PACKAGE = 'users'

DOWNLOAD_PATH = os.environ['HOME'] + '/the-mad-monkey/'

FILE_ERROR_FORWARD_MSG = '⚠️ File too big! Trying to download it using the client. File name: '
