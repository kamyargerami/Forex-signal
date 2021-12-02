import sys
from datetime import datetime

from api_providers.alphavantage import alphavantage
from api_providers.twelvedata import twelvedata
from telegram import telegram

provider = sys.argv[1] if len(sys.argv[1:]) else 'twelvedata'

print('--------------------------------')
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '-', provider)
results = twelvedata().result() if provider == 'twelvedata' else alphavantage().result()
print('--------------------------------')

if not len(results):
    exit()

text = '📊 RSI Choices in Weekly Rates: \n\n'
buttons = []
for result in results:
    buttons.append([{
        'text': '%s (%s)' % (result['symbol'], result['daily_rate']),
        'url': 'https://www.tradingview.com/chart?symbol=FX%3A' + result['symbol'].replace('/', '')
    }])

    text += '%s (%s) - %s \n ------------ \n' % (
        result['symbol'], result['weekly_rate'], ('Buy ⬆️' if result['weekly_rate'] < 35 else 'Sell ⬇️'))
text += '\n Their Daily Rates:'

telegram.send(text, buttons, {
    # 'http': 'http://127.0.0.1:1080',
    # 'https': 'http://127.0.0.1:1080',
})
