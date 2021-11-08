from datetime import datetime
import requests
import json

class telegram:
    def send(text, buttons = [], proxies = {}):
        return requests.post('https://api.telegram.org/bot2138363040:AAHm-3hcFSPMLIgj9XvR6pOk1T6MkZpL2xM/sendMessage',{
            'chat_id': '-1001639596478',
            'text': text,
            'reply_markup': json.dumps({
                'inline_keyboard': buttons
            })
        }, proxies=proxies, timeout=10)