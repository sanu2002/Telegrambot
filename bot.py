import requests
MESSAGE = 'Hello from GitHub Actions!'

url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
payload = {'chatid': CHAT_ID, 'text': MESSAGE}

response = requests.post(url, json=payload)
print(response.json())
