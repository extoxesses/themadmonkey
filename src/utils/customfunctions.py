#!/usr/bin/env python
# This is an utility library for custom functions

import sys
sys.path.append('src/')

import constants

import logging
import os

logging.basicConfig(format=constants.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger(constants.MAIN)



def isTorrent(filename) :
  return (filename.split('.')[-1] == 'torrent')


def startTorrentDownload(filepath) :
  os.system('transmission-remote -a' + filepath)
