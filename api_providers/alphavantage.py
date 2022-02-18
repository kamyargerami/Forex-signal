import requests
from dotenv import dotenv_values

from api_providers.provider import provider

config = dotenv_values(".env")


class Alphavantage(provider):
    symbols = ['EURUSD', 'USDJPY', 'GBPUSD', 'AUDUSD', 'USDCAD', 'USDCHF', 'NZDUSD', 'EURGBP', 'EURAUD', 'EURCHF',
               'EURJPY', 'EURNZD', 'GBPEUR', 'GBPJPY', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPNZD', 'CADCHF', 'CADJPY']

    def get_rate(self, symbol, interval, indicator='RSI', time_period=14):
        response = requests.get(
            'https://www.alphavantage.co/query?function=%s&symbol=%s&interval=%s&time_period=%d&series_type=close&apikey=%s'
            % (indicator, symbol, interval, time_period, config['ALPHAVANTAGE_API_KEY']), timeout=5)

        results = response.json().get('Technical Analysis: RSI')

        if not results:
            print(results)
            return False

        return float(next(iter(results.values()))[indicator])

    def get_hourly_rsi_rate(self, symbol):
        return self.get_rate(symbol, '60min')

    def get_daily_rsi_rate(self, symbol):
        return self.get_rate(symbol, 'daily')

    def get_weekly_rsi_rate(self, symbol):
        return self.get_rate(symbol, 'weekly')

    def get_hourly_cci_rate(self, symbol):
        return self.get_rate(symbol, '60min', 'CCI', 20)

    def get_daily_cci_rate(self, symbol):
        return self.get_rate(symbol, 'daily', 'CCI', 20)

    def get_weekly_cci_rate(self, symbol):
        return self.get_rate(symbol, 'weekly', 'CCI', 20)

    def get_hourly_mfi_rate(self, symbol):
        return self.get_rate(symbol, '60min', 'MFI')

    def get_daily_mfi_rate(self, symbol):
        return self.get_rate(symbol, 'daily', 'MFI')

    def get_weekly_mfi_rate(self, symbol):
        return self.get_rate(symbol, 'weekly', 'MFI')
