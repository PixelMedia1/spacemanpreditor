from telegram.ext import Updater, CommandHandler
from slot_scraper import scrape_slot_data
from predictor import predict_slot_outcome

# Token API bot Telegram
TOKEN = '7053528679:AAGzRWfsKxaFAfIv14x_EUywazzG4Bil9fE'

def start(update, context):
    update.message.reply_text('Welcome to Spaceman Predictor Bot! Use /predict to get a prediction.')

def predict(update, context):
    # Scraping data from the slot website
    slot_data = scrape_slot_data()

    # Predicting the outcome using Spaceman predictor
    prediction = predict_slot_outcome(slot_data)

    # Sending the prediction as a message
    update.message.reply_text(f'Prediction: {prediction}')

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("predict", predict))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if _name_ == '_main_':
    main()