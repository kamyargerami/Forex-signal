import time


class provider:
    symbols = list

    def get_rate(self, symbol, interval):
        pass

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

            time.sleep(15)

            hourly_rate = self.get_hourly_rsi_rate(symbol)
            print('Hourly rate:', hourly_rate)

            if not hourly_rate:
                continue
            if (hourly_rate < 73 and hourly_rate > 27):
                continue
            if (hourly_rate > 27 and hourly_rate < 73):
                continue

            daily_rate = self.get_daily_rsi_rate(symbol)
            print('Daily rate:', daily_rate)

            if not daily_rate:
                continue

            result.append({'symbol': symbol, 'hourly_rate': hourly_rate, 'daily_rate': daily_rate})

        return result
