#!/usr/bin/env python
#
# This is an utility class including methods for users management


from constants.bot_constants import BotConstants

import logging
logging.basicConfig(format=BotConstants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(BotConstants.USERS_PACKAGE)


class UsersUtils :

  def checkUser(user, whitelist) :
    try:
      name = whitelist[user.id]
      LOGGER.info('Valid request from ' + name)
      return True

    except KeyError as e:
      LOGGER.warn ('Invalid request form ' + user.first_name)
      return False
