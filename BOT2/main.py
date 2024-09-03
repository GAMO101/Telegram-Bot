import requests

token = '7320474822:AAGCjrT2ggUSSliSfaf6QTfElv4dwh7ouq4'
method = "sendMessage"

response = requests.post(
    url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
    data={'chat_id': -1002230118853, 'text': 'hello friend'}
).json()