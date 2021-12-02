import time

class provider:
    symbols = list
    
    def get_hourly_rsi_rate(self, symbol):
        pass

    def get_daily_rsi_rate(self, symbol):
        pass

    def get_weekly_rsi_rate(self, symbol):
        pass

    def result(self):
        result = []

        for symbol in self.symbols:
            print('**************')
            print(symbol)

            time.sleep(20)

            weekly_rate = self.get_weekly_rsi_rate(symbol)
            print('Weekly rate:', weekly_rate)

            if not weekly_rate:
                continue
            if (weekly_rate < 67 and weekly_rate > 33):
                continue
            if (weekly_rate > 33 and weekly_rate < 67):
                continue

            daily_rate = self.get_daily_rsi_rate(symbol)
            print('Daily rate:', daily_rate)

            if not daily_rate:
                continue

            result.append({'symbol': symbol, 'weekly_rate': weekly_rate, 'daily_rate': daily_rate})
            
        return result
