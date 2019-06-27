FROM python:3.5

ADD src /
ADD environments /environments


RUN pip install telegram
RUN pip3 install python-telegram-bot
RUN pip3 install pyrogram
RUN pip3 install python-dotenv

CMD [ "python3", "./the-mad-monkey.py", "./environments/bot.env" ]
CMD [ "python3", "./client.py", "./environments/bot.env" ]
