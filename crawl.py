import sys
from datetime import datetime

from api_providers.alphavantage import Alphavantage
from api_providers.twelvedata import Twelvedata
from telegram import telegram


def send_notify(results):
    text = '📊 Forex Paris Signals \n\n'

    buttons = []
    for result in results:
        buttons.append([{
            'text': result['symbol'],
            'url': 'https://www.tradingview.com/chart?symbol=FX%3A' + result['symbol'].replace('/', '')
        }])

    telegram.send(text, buttons, {
        # 'http': 'socks5h://127.0.0.1:1080',
        # 'https': 'socks5h://127.0.0.1:1080'
    })


provider = sys.argv[1] if len(sys.argv[1:]) else 'twelvedata'

print('--------------------------------')
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '-', provider)
results = Twelvedata().get_result() if provider == 'twelvedata' else Alphavantage().get_result()
print('--------------------------------')

if not len(results):
    print('No results')
    exit()

send_notify(results)
