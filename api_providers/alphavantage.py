import requests
from api_providers.provider import provider

class alphavantage(provider):
    ## 20 symbols support per hour - 17 added
    symbols = ['EURUSD', 'USDJPY', 'GBPUSD', 'AUDUSD', 'USDCAD', 'USDCHF', 'NZDUSD', 'EURGBP', 'EURAUD', 'EURCHF', 'EURJPY', 'EURNZD', 'GBPEUR', 'GBPJPY', 'GBPAUD', 'GBPCAD', 'GBPCHF']

    def get_hourly_rsi_rate(self, symbol):
        response = requests.get('https://www.alphavantage.co/query?function=RSI&symbol=%s&interval=60min&time_period=14&series_type=close&apikey=MVS8TN4ZTQF1ONES' % symbol)
        results = response.json().get('Technical Analysis: RSI')
    
        if not results:
            print(results)
            return False
        return float(next(iter(results.values()))['RSI'])

    def get_daily_rsi_rate(self, symbol):
        response = requests.get('https://www.alphavantage.co/query?function=RSI&symbol=%s&interval=daily&time_period=14&series_type=close&apikey=MVS8TN4ZTQF1ONES' % symbol)
        results = response.json().get('Technical Analysis: RSI')
    
        if not results:
            print(results)
            return False
        return float(next(iter(results.values()))['RSI'])