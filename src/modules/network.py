#!/usr/bin/env python
# Network services

import sys
sys.path.append('src/')
import constants, logging, urllib

logging.basicConfig(format=constants.LOGGER_FORMAT, level=logging.INFO)
logger = logging.getLogger(constants.NETWORK_PACKAGE)

def whoYouAre(update, context):
    request = urllib.urlopen('https://ident.me')
    response = ''
    for line in request:
        response = response + line

    logger.info('Public ip: ' + response)
    context.message.reply_text('You are ' + response)

