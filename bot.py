import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Enable logging to see if there are any errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)  # Set logging level to DEBUG to see detailed logs
logger = logging.getLogger(__name__)

# Get the Telegram bot token from environment variable (e.g., GitHub secrets)
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Get the token from GitHub secrets

if TELEGRAM_BOT_TOKEN is None:
    logger.error("Error: TELEGRAM_BOT_TOKEN is not set.")
    exit(1)

# Define the /start command handler
async def start(update: Update, context: CallbackContext) -> None:
    logger.info(f"Received /start command from user: {update.effective_user.first_name}")
    user = update.effective_user  # Get the user who triggered the /start command
    chat_id = update.message.chat_id  # Get the chat ID automatically from the update object

    # Send a welcome message to the user who triggered the /start command
    await update.message.reply_text(f"Hello, {user.first_name}! Welcome to the bot.")

def main():
    # Create the Application and pass the bot's token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot (async)
    application.run_polling()

if __name__ == '__main__':
    main()
