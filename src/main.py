import telebot
import logging
from command import Command
import subprocess

bot = telebot.TeleBot('7939669010:AAEG8-KmNSVoisckbRFYM36Kq2-HkXJZWrU')

botlog = telebot.logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filemode="w", format="%(asctime)s %(levelname)s %(message)s\n" + str(botlog))


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "test start")

@bot.message_handler(commands=["test"])
def start(message):
    bot.send_message(message.chat.id, str(Command.get_uptime()))

if __name__ == '__main__':
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
