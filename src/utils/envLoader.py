#!/usr/bin/env python
# Environment configurations loader

from pyrogram import Client

class EnvLoader :
  
  # Bot configuration variables
  BOT_NAME = 'TMM_BOT_NAME'
  TOKEN = 'TMM_TOKEN'

  # Client app configuration
  CLIENT_API_ID = 'TMM_CLIENT_API_ID'
  CLIENT_API_HASH = 'TMM_CLIENT_API_HASH'

  # Telegram owner user configuration
  OWNER_ID = 'TMM_OWNER_ID'
  OWNER_NAME = 'TMM_OWNER_NAME'
  
  # Telegram APIs configuration
  API_ID = 'TMM_API_ID'
  API_HASH = 'TMM_API_HASH'



  """This method instantiate the bypass client

  :returns: A client istance
  :rtype: pyrogram.Client object
  """
  def getClient() :
    return Client (
      OWNER_NAME,
      api_id=API_ID,
      api_hash=API_HASH
    )



  """This method returs the map of the default allowed users

  :returns: Allowed users map
  :rtype: dict
  """
  def getValidUsers() :
    return {OWNER_ID : OWNER_NAME}