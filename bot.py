import requests
CHATID = '6662820897'
MESSAGE = 'Hello from GitHub Actions!'

url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
payload = {'chatid': CHATID, 'text': MESSAGE}

response = requests.post(url, json=payload)
print(response.json())
