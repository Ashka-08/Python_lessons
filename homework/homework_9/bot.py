import logging
from config import TOKEN
from telegram import *
from telegram.ext import *
from random import randint

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет, я бот, умею генерировать пароли:\n/random_digits")

def random_digits(update, context):
    password = randint(100000, 1000000)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=f'Сгенерирован пароль: \n{password}')

updater = Updater(TOKEN)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

random_d = CommandHandler('random_digits', random_digits)
dispatcher.add_handler(random_d)

updater.start_polling()