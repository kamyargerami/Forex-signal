import requests
from api_providers.provider import provider
from datetime import datetime

class twelvedata(provider):
    ## 33 symbols support per hour - 24 added
    symbols = ['EUR/USD', 'USD/JPY', 'GBP/USD', 'AUD/USD', 'USD/CAD', 'USD/CHF', 'NZD/USD', 'EUR/GBP', 'EUR/AUD', 'EUR/CHF', 'EUR/JPY', 'EUR/NZD', 'GBP/EUR', 'GBP/JPY', 'GBP/AUD', 'GBP/CAD', 'GBP/CHF', 'GBP/NZD', 'FB', 'IBM', 'AAPL', 'PEP', 'BABA', 'MSFT']

    def get_hourly_rsi_rate(self, symbol):
        response = requests.get('https://api.twelvedata.com/rsi?symbol=%s&interval=1h&apikey=f4ca8bae96fe4fd88717d7bdbbba1d37' % symbol)
        results = response.json().get('values')
    
        if not results:
            print(results)
            return False

        return float(next(iter(results))['rsi'])

    def get_daily_rsi_rate(self, symbol):
        if (symbol in ['FB', 'IBM', 'AAPL', 'PEP', 'COKE', 'BABA', 'MSFT']) and (int(datetime.now().strftime("%H")) < 17):
            print('Market not oppened yet')
            return False

        response = requests.get('https://api.twelvedata.com/rsi?symbol=%s&interval=1day&apikey=f4ca8bae96fe4fd88717d7bdbbba1d37' % symbol)
        results = response.json().get('values')
    
        if not results:
            print(results)
            return False
            
        return float(next(iter(results))['rsi'])