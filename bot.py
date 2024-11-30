import requests
TOKEN = "6662820897:AAF_IaDV4a2-ZCGiCF4jrRTvTK4XbmgpzMc"
CHATID = '6662820897'
MESSAGE = 'Hello from GitHub Actions!'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
payload = {'chatid': CHATID, 'text': MESSAGE}

response = requests.post(url, json=payload)
print(response.json())
