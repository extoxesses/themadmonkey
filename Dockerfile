FROM python:3.5

WORKDIR /the-mad-monkey-bot


COPY . /the-mad-monkey-bot
RUN ["chmod", "+x", "/the-mad-monkey-bot/scripts/run.sh"]


RUN pip install telegram
RUN pip3 install python-telegram-bot
RUN pip3 install pyrogram
RUN pip3 install python-dotenv

# This package is needed to increase bot speed
RUN pip3 install -U tgcrypto

CMD ["/bin/sh", "-c", "/the-mad-monkey-bot/scripts/run.sh /the-mad-monkey-bot"]
