#!/usr/bin/env python
# This is an utility class including methods for users management

import sys
sys.path.append('src/')

import constants

import logging

logging.basicConfig(format=constants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(constants.MAIN)


def checkUser(user, whitelist) :
  try:
    name = whitelist[user.id]
    LOGGER.info('Valid request from ' + name)
    return True

  except KeyError as e:
    LOGGER.warn ('Invalid request form ' + user.first_name)
    return False
