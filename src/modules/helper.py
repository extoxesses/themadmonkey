#!/usr/bin/env python
# Help endpoints

import sys
sys.path.append('resources')
import reserved

def hi(update, context):
    user_id = context['message']['chat']['id']
    try:
        user_tag = reserved.VALID_USERS[user_id]
        context.message.reply_text('Hi, ' + user_tag + '!')
    except KeyError as e:
        context.message.reply_text('Who are you?')


