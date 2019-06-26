#!/usr/bin/env python
#
# This class allows to load env configuration variables


from os import environ
from dotenv import load_dotenv

# Load configuration variables
load_dotenv('./environments/bot.env')



class Config :

    BOT_NAME = environ['TMM_BOT_NAME']
    TOKEN = environ['TMM_TOKEN']
    
    OWNER_ID = environ['TMM_OWNER_ID']
    OWNER_NAME = environ['TMM_OWNER_NAME']
    
    API_ID = environ['TMM_API_ID']
    API_HASH = environ['TMM_API_HASH']
    
    CLIENT_API_ID = environ['TMM_CLIENT_API_ID']
    CLIENT_API_HASH = environ['TMM_CLIENT_API_HASH']
