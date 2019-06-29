#!/bin/sh

clear
echo ">>> Creating docker image..."
echo ""

sudo docker build -t exto/themadmonkey .

echo ""
echo "-----------------------------"
echo ">>> Running building image..."
echo ""

sudo docker run -v ~/Downloads/themadmonkey :/the-mad-monkey-bot/downloads -it exto/themadmonkey
