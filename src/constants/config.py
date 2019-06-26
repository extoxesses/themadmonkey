#!/usr/bin/env python
#
# This class allows to load env configuration variables

from os import environ
from dotenv import load_dotenv


class Config :
  def __init__(self, path) :
    load_dotenv(path)

    self.BOT_NAME = environ['TMM_BOT_NAME']
    self.TOKEN = environ['TMM_TOKEN']
    
    self.OWNER_ID = environ['TMM_OWNER_ID']
    self.OWNER_NAME = environ['TMM_OWNER_NAME']
    
    self.API_ID = environ['TMM_API_ID']
    self.API_HASH = environ['TMM_API_HASH']
    
    self.CLIENT_API_ID = environ['TMM_CLIENT_API_ID']
    self.CLIENT_API_HASH = environ['TMM_CLIENT_API_HASH']
