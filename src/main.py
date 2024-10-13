import telebot
import logging
from command import Command
import subprocess
import time
from collections import deque
import os

bot = telebot.TeleBot('7939669010:AAEG8-KmNSVoisckbRFYM36Kq2-HkXJZWrU')

botlog = telebot.logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filemode="w", format="%(asctime)s %(levelname)s %(message)s\n" + str(botlog))

text_session: str = "New session"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "test start")

@bot.message_handler(commands=["test"])
def start(message):
    bot.send_message(message.chat.id, str(Command.get_uptime()))

@bot.message_handler(commands=["test_pars"])
def start(message):
    while os.path.isfile("/var/log/auth.log"):
        with open('/var/log/auth.log', 'r') as file:
            for line in file:
                [last_line] = deque(file, maxlen=1) or ['']
                if text_session in last_line:
                    bot.send_message(message.chat.id, str(last_line))
                time.sleep(10)

if __name__ == '__main__':
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
