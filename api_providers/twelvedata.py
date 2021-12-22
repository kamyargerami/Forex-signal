from datetime import datetime

import requests

from api_providers.provider import provider


class twelvedata(provider):
    symbols = ['EUR/USD', 'USD/JPY', 'GBP/USD', 'AUD/USD', 'USD/CAD', 'USD/CHF', 'NZD/USD', 'EUR/GBP', 'EUR/AUD',
               'EUR/CHF', 'EUR/JPY', 'EUR/NZD', 'GBP/EUR', 'GBP/JPY', 'GBP/AUD', 'GBP/CAD', 'GBP/CHF', 'GBP/NZD',
               'CAD/CHF', 'CAD/JPY', 'FB', 'IBM', 'AAPL', 'PEP', 'BABA', 'MSFT']

    def get_rate(self, symbol, interval):
        if (symbol in ['FB', 'IBM', 'AAPL', 'PEP', 'COKE', 'BABA', 'MSFT']) and (
                int(datetime.now().strftime("%H")) < 17):
            print('Market not oppened yet')
            return False

        response = requests.get(
            'https://api.twelvedata.com/rsi?symbol=%s&interval=%s&apikey=f4ca8bae96fe4fd88717d7bdbbba1d37' % (
                symbol, interval))
        results = response.json().get('values')

        if not results:
            print(results)
            return False

        return float(next(iter(results))['rsi'])

    def get_hourly_rsi_rate(self, symbol):
        return self.get_rate(symbol, '1h')

    def get_daily_rsi_rate(self, symbol):
        return self.get_rate(symbol, '1day')

    def get_weekly_rsi_rate(self, symbol):
        return self.get_rate(symbol, '1week')
