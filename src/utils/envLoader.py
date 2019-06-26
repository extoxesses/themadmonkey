#!/usr/bin/env python
#
# Environment configurations loader

from pyrogram import Client
from constants.config import Config



class EnvLoader :

  """This method instantiate the bypass client

  :returns: A client istance
  :rtype: pyrogram.Client object
  """
  def getClient() :
    return Client (
      Config.OWNER_NAME,
      api_id=Config.API_ID,
      api_hash=Config.API_HASH
    )



  """This method returs the map of the default allowed users

  :returns: Allowed users map
  :rtype: dict
  """
  def getValidUsers() :
    return {Config.OWNER_ID : Config.OWNER_NAME}