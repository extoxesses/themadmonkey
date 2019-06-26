#!/usr/bin/env python
# This is an utility library for custom functions

import constants as CONSTS

import logging
from os import environ

logging.basicConfig(format=CONSTS.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(CONSTS.CUSTOM_PACKAGE)



def isTorrent(filename) :
  return (filename.split('.')[-1] == 'torrent')


def startTorrentDownload(filepath) :
  system('transmission-remote -a' + filepath)
