# команда для установки бота в терминале 
# pip install python-telegram-bot --pre

# название бота
# its_alive_my_new_python_bot

# Use this token to access the HTTP API:
# 5878100508:AAG-06PEv6e7y96rcLEUuS5FsDi7Z1VskI0

# команда для запуска бота из терминала 
# python bot_code.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5878100508:AAG-06PEv6e7y96rcLEUuS5FsDi7Z1VskI0").build()

app.add_handler(CommandHandler("hello", hello))
print('Server start')
app.run_polling()