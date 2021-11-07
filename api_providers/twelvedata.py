import requests
from api_providers.provider import provider

class twelvedata(provider):
    symbols = ['EUR/USD', 'USD/JPY']

    def get_hourly_rsi_rate(self, symbol):
        response = requests.get('https://api.twelvedata.com/rsi?symbol=%s&interval=1h&apikey=f4ca8bae96fe4fd88717d7bdbbba1d37' % symbol)
        results = response.json().get('values')
    
        if not results:
            print(results)
            return False

        return float(next(iter(results))['rsi'])

    def get_daily_rsi_rate(self, symbol):
        response = requests.get('https://api.twelvedata.com/rsi?symbol=%s&interval=1day&apikey=f4ca8bae96fe4fd88717d7bdbbba1d37' % symbol)
        results = response.json().get('values')
    
        if not results:
            print(results)
            return False
            
        return float(next(iter(results))['rsi'])