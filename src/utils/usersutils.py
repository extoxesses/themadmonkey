#!/usr/bin/env python
# This is an utility class including methods for users management

import src.constants

import logging


logging.basicConfig(format=src.constants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(src.constants.USERS_PACKAGE)


def checkUser(user, whitelist) :
  try:
    name = whitelist[user.id]
    LOGGER.info('Valid request from ' + name)
    return True

  except KeyError as e:
    LOGGER.warn ('Invalid request form ' + user.first_name)
    return False
