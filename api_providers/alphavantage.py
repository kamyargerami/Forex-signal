import requests

from api_providers.provider import provider


class alphavantage(provider):
    symbols = ['EURUSD', 'USDJPY', 'GBPUSD', 'AUDUSD', 'USDCAD', 'USDCHF', 'NZDUSD', 'EURGBP', 'EURAUD', 'EURCHF',
               'EURJPY', 'EURNZD', 'GBPEUR', 'GBPJPY', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPNZD', 'CADCHF', 'CADJPY']

    def get_rate(self, symbol, interval):
        response = requests.get(
            'https://www.alphavantage.co/query?function=RSI&symbol=%s&interval=%s&time_period=14&series_type=close&apikey=MVS8TN4ZTQF1ONES'
            % (symbol, interval))

        results = response.json().get('Technical Analysis: RSI')

        if not results:
            print(results)
            return False

        return float(next(iter(results.values()))['RSI'])

    def get_hourly_rsi_rate(self, symbol):
        return self.get_rate(symbol, '60min')

    def get_daily_rsi_rate(self, symbol):
        return self.get_rate(symbol, 'daily')

    def get_weekly_rsi_rate(self, symbol):
        return self.get_rate(symbol, 'weekly')
