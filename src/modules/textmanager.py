#!/usr/bin/env python
# Endpoints for non-command messages management

import sys
sys.path.append('resources')
import reserved


class TextManager:
  def __init__(self, bot):
    self.bot = bot

  def manageText(bot, update, context):
    context.message.reply_text(context.message.text)
