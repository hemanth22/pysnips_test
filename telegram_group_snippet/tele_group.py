import requests
import os

bot_token = os.environ.get('Priyoid_bot')

#message = "Hello World!"

with open('remainder_today.txt','r') as file:
    file_contents = file.read()

message = file_contents


def telegram_send_message(message):
    url = "https://api.telegram.org/bot{}/sendMessage?chat_id=-1001943848370&text={}".format(bot_token, message)
    requests.get(url)

#telegram_send_message(message)
for new_sendMessage_tele in message.split("\n"):
    telegram_send_message(new_sendMessage_tele)
