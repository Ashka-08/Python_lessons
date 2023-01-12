from config import TOKEN

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from random import randint
from random import choice
import string

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Привет, я бот! Умею генерировать пароли.")
    keyboard = [
        [
            InlineKeyboardButton("Из чисел", callback_data='Из чисел'),
            InlineKeyboardButton("Из букв", callback_data='Из букв'),
        ],
        [InlineKeyboardButton("Из букв и чисел", callback_data='Из букв и чисел')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # context.bot.send_message(chat_id=update.effective_chat.id, text="Меню из двух столбцов", reply_markup=reply_markup)
    update.message.reply_text('Пожалуйста, выберите:', reply_markup=reply_markup)

def random_digits():
    return randint(1000000, 10000000)

def random_letters():
    password = ''
    for i in range(8):
        l = choice(string.ascii_letters)
        password += l
    return password

def full_random():
    password = []
    f = [0, 1]
    for i in range(8):
        el = choice(f)
        if el == 0:
            l = choice(string.ascii_letters)
            password.append(l)
        elif el == 1:
            l = randint(0, 9)
            password.append(l)
    password = [str(i) for i in password]
    password = "".join(password)
    return password

def button(update, context):
    query = update.callback_query
    variant = query.data
    query.answer()
    # вариант редактирования сообщения, тем самым кнопки в чате заменятся на этот ответ.
    # query.edit_message_text(text=f"Выбранный вариант: {variant}")
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=f"Выбранный вариант: {variant}")
    logger.info("Выбор операции: %s: %s", update.effective_user.first_name, variant)
    if variant == 'Из чисел':
        ansver = random_digits()
        context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=ansver)
    elif variant == 'Из букв':
        ansver = random_letters()
        context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=ansver)
    elif variant == 'Из букв и чисел':
        ansver = full_random()
        context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=ansver)
    logger.info("Сгенерирован пароль: %s: %s", update.effective_user.first_name, ansver)

def help_command(update, _):
    update.message.reply_text("Используйте /start` для тестирования.")


if __name__ == '__main__':

    updater = Updater(TOKEN)
    app = updater.dispatcher

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler('help', help_command))

    updater.start_polling()
    updater.idle()
