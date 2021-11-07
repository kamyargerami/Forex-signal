import time
import json
import requests
from datetime import datetime

symbols = ['EURUSD', 'USDJPY', 'GBPUSD', 'AUDUSD', 'USDCAD', 'USDCHF', 'NZDUSD', 'EURGBP', 'EURAUD', 'EURCHF', 'EURJPY', 'EURNZD', 'GBPEUR', 'GBPJPY', 'GBPAUD', 'GBPCAD', 'GBPCHF']

def get_hourly_rsi_rate(symbol):
    response = requests.get('https://www.alphavantage.co/query?function=RSI&symbol=%s&interval=60min&time_period=14&series_type=close&apikey=MVS8TN4ZTQF1ONES' % symbol)
    results = response.json().get('Technical Analysis: RSI')
    
    if not results:
        print(results)
        return False
    return float(next(iter(results.values()))['RSI'])

def get_daily_rsi_rate(symbol):
    response = requests.get('https://www.alphavantage.co/query?function=RSI&symbol=%s&interval=daily&time_period=14&series_type=close&apikey=MVS8TN4ZTQF1ONES' % symbol)
    results = response.json().get('Technical Analysis: RSI')
    
    if not results:
        print(results)
        return False
    return float(next(iter(results.values()))['RSI'])

    
def get_result():
    result = []
    for symbol in symbols:
        print('**************')
        print(symbol)

        time.sleep(12)

        daily_rate = get_daily_rsi_rate(symbol)
        print('Daily rate:', daily_rate)

        if not daily_rate:
            continue
        if (daily_rate < 65 and daily_rate > 35):
            continue
        if (daily_rate > 35 and daily_rate < 65):
            continue

        hourly_rate = get_hourly_rsi_rate(symbol)
        print('Hourly rate:', hourly_rate)

        if not hourly_rate:
            continue
        if (hourly_rate < 55 and hourly_rate > 40):
            continue
        if (hourly_rate > 40 and hourly_rate < 55):
            continue

        result.append({'symbol': symbol, 'hour_rate': hourly_rate, 'daily_rate': daily_rate})
    return result

def get_current_date_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def send_telegram_notify(result, proxies = {}):
    inline_keyboard = []

    for result in results:
        inline_keyboard.append({
            'text': result['symbol'] + ' - ' + ('Buy ⬆️' if result['daily_rate'] < 35 else 'Sell ⬇️'),
            'url': 'https://www.tradingview.com/chart?symbol=FX%3A' + result['symbol']
        })

    response = requests.post('https://api.telegram.org/bot2138363040:AAHm-3hcFSPMLIgj9XvR6pOk1T6MkZpL2xM/sendMessage',{
        'chat_id': '-1001639596478',
        'text': get_current_date_time(),
        'reply_markup': json.dumps({
            'inline_keyboard': [inline_keyboard]
        })
    }, proxies=proxies, timeout=10)    

print('--------------------------------')
print(get_current_date_time())
results = get_result()
print('--------------------------------')

if not len(results):
    exit()

send_telegram_notify(results, {
    # 'http': 'http://127.0.0.1:1080',
    # 'https': 'http://127.0.0.1:1080' 
})