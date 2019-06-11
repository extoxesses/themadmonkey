#!/usr/bin/env python
# This is an utility library for custom functions

import src.constants

import logging
import os

logging.basicConfig(format=src.constants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(src.constants.CUSTOM_PACKAGE)



def isTorrent(filename) :
  return (filename.split('.')[-1] == 'torrent')


def startTorrentDownload(filepath) :
  os.system('transmission-remote -a' + filepath)
