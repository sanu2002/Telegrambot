import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Get the Telegram bot token from GitHub Secrets
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Access the secret from GitHub Secrets

if TELEGRAM_BOT_TOKEN is None:
    print("Error: TELEGRAM_BOT_TOKEN is not set.")
    exit(1)

# Set up logging to see any errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the /start command handler
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    # Send a welcome message when the /start command is issued
    update.message.reply_text(f"Hello, {user.first_name}! Welcome to the bot.")

def main():
    # Create the Updater and pass the bot's token
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
