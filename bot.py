import requests
MESSAGE = 'Hello from GitHub Actions!'
# Get the Telegram bot token and chat ID from GitHub Secrets (stored as environment variables)
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Access the secret from GitHub Secrets
CHAT_ID = os.getenv('CHAT_ID')  # Access the secret from GitHub Secrets


url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
payload = {'chatid': CHAT_ID, 'text': MESSAGE}

response = requests.post(url, json=payload)
print(response.json())
