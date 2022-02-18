import json

import requests
from dotenv import dotenv_values

config = dotenv_values(".env")  #


class telegram:
    def send(text, buttons=[], proxies={}):
        return requests.post('https://api.telegram.org/bot' + config['TELEGRAM_BOT_TOKEN'] + '/sendMessage', {
            'chat_id': config['TELEGRAM_CHAT_ID'],
            'text': text,
            'reply_markup': json.dumps({
                'inline_keyboard': buttons
            })
        }, proxies=proxies, timeout=10)
