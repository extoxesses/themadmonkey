#!/usr/bin/env python
#
# Environment configurations loader

from pyrogram import Client


class EnvLoader :

  """This method instantiate the bypass client

  :returns: A client istance
  :rtype: pyrogram.Client object
  """
  def getClient(self, config) :
    return Client (
      config.OWNER_NAME,
      api_id=config.API_ID,
      api_hash=config.API_HASH
    )



  """This method returs the map of the default allowed users

  :returns: Allowed users map
  :rtype: dict
  """
  def getValidUsers(self, config) :
    return {config.OWNER_ID : config.OWNER_NAME}