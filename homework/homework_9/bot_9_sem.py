import logging
from config import TOKEN
from telegram import *
from telegram.ext import *
import random
import string

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет, я бот! Умею генерировать пароли:\n"
                             "из чисел -> /random_digits\n"
                             "из букв -> /random_letters\n"
                             "из букв и чисел -> /full_random")

def random_digits(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    password = random.randint(1000000, 10000000)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=f'Сгенерирован пароль: \n{password}')

def random_letters(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    password = ''
    for i in range(8):
        l = random.choice(string.ascii_letters)
        password += l
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=f'Сгенерирован пароль: \n{password}')

def full_random(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    password = []
    f = [0, 1]
    for i in range(8):
        el = random.choice(f)
        if el == 0:
            l = random.choice(string.ascii_letters)
            password.append(l)
        elif el == 1:
            l =random.randint(0, 9)
            password.append(l)
    password = [str(i) for i in password]
    password = "".join(password)
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=f'Сгенерирован пароль: \n{password}')

updater = Updater(TOKEN)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

random_d = CommandHandler('random_digits', random_digits)
dispatcher.add_handler(random_d)

random_l = CommandHandler('random_letters', random_letters)
dispatcher.add_handler(random_l)

random_f = CommandHandler('full_random', full_random)
dispatcher.add_handler(random_f)

updater.start_polling()