from datetime import datetime

import requests
from dotenv import dotenv_values

from api_providers.provider import provider

config = dotenv_values(".env")


class Twelvedata(provider):
    symbols = ['EUR/USD', 'USD/JPY', 'GBP/USD', 'AUD/USD', 'USD/CAD', 'USD/CHF', 'NZD/USD', 'EUR/GBP', 'EUR/AUD',
               'EUR/CHF', 'EUR/JPY', 'EUR/NZD', 'GBP/EUR', 'GBP/JPY', 'GBP/AUD', 'GBP/CAD', 'GBP/CHF', 'GBP/NZD',
               'CAD/CHF', 'CAD/JPY', 'FB', 'IBM', 'AAPL', 'PEP', 'BABA', 'MSFT']

    def get_rate(self, symbol, interval, indicator='rsi', time_period=14):
        if (symbol in ['FB', 'IBM', 'AAPL', 'PEP', 'COKE', 'BABA', 'MSFT']) and (
                int(datetime.now().strftime("%H")) < 17):
            print('Market not oppened yet')
            return False

        response = requests.get(
            'https://api.twelvedata.com/%s?symbol=%s&interval=%s&time_period=%d&apikey=%s' % (
                indicator, symbol, interval, time_period, config['TWELVEDATA_API_KEY']), timeout=5)
        results = response.json().get('values')

        if not results:
            print(results)
            return False

        return float(next(iter(results))[indicator])

    def get_hourly_rsi_rate(self, symbol):
        return self.get_rate(symbol, '1h')

    def get_daily_rsi_rate(self, symbol):
        return self.get_rate(symbol, '1day')

    def get_weekly_rsi_rate(self, symbol):
        return self.get_rate(symbol, '1week')

    def get_hourly_cci_rate(self, symbol):
        return self.get_rate(symbol, '1h', 'cci', 20)

    def get_daily_cci_rate(self, symbol):
        return self.get_rate(symbol, '1day', 'cci', 20)

    def get_weekly_cci_rate(self, symbol):
        return self.get_rate(symbol, '1week', 'cci', 20)

    def get_hourly_mfi_rate(self, symbol):
        return self.get_rate(symbol, '1h', 'mfi')

    def get_daily_mfi_rate(self, symbol):
        return self.get_rate(symbol, '1day', 'mfi')

    def get_weekly_mfi_rate(self, symbol):
        return self.get_rate(symbol, '1week', 'mfi')
