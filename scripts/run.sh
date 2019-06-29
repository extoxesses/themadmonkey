#!/bin/sh

python3 $1/src/client.py ./environments/bot.env &

python3 $1/src/the-mad-monkey.py ./environments/bot.env
