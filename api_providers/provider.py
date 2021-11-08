import time

class provider:
    symbols = list
    
    def get_hourly_rsi_rate(self, symbol):
        pass

    def get_daily_rsi_rate(self, symbol):
        pass

    def result(self):
        result = []

        for symbol in self.symbols:
            print('**************')
            print(symbol)

            time.sleep(12)

            daily_rate = self.get_daily_rsi_rate(symbol)
            print('Daily rate:', daily_rate)

            if not daily_rate:
                continue
            if (daily_rate < 65 and daily_rate > 35):
                continue
            if (daily_rate > 35 and daily_rate < 65):
                continue

            hourly_rate = self.get_hourly_rsi_rate(symbol)
            print('Hourly rate:', hourly_rate)

            if not hourly_rate:
                continue

            result.append({'symbol': symbol, 'hour_rate': hourly_rate, 'daily_rate': daily_rate})
            
        return result
