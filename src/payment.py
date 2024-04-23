from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import logging

# Setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(_name_)

# Token bot telegram
TOKEN = "7053528679:AAGzRWfsKxaFAfIv14x_EUywazzG4Bil9fE"

# List item yang tersedia untuk pembelian
items = [
    {"name": "Item 1", "price": 10},
    {"name": "Item 2", "price": 20},
    {"name": "Item 3", "price": 30}
]

def start(update, context):
    user = update.effective_user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {user.first_name}! Welcome to our bot.")

def list_items(update, context):
    keyboard = []
    for item in items:
        keyboard.append([InlineKeyboardButton(f"{item['name']} - ${item['price']}", callback_data=item['name'])])
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose an item to purchase:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()

    for item in items:
        if query.data == item['name']:
            query.message.reply_text(f"You have chosen: {item['name']} - ${item['price']}. Proceed with payment...")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("list", list_items))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if _name_ == '_main_':
    main()