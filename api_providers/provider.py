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

    def get_hourly_cci_rate(self, symbol):
        pass

    def get_daily_cci_rate(self, symbol):
        pass

    def get_weekly_cci_rate(self, symbol):
        pass

    def get_hourly_mfi_rate(self, symbol):
        pass

    def get_daily_mfi_rate(self, symbol):
        pass

    def get_weekly_mfi_rate(self, symbol):
        pass

    def is_good_rsi_rate(self, rate):
        if not rate:
            return False
        if (70 > rate > 30) or (30 < rate < 70):
            return False
        return True

    def is_good_cci_rate(self, rate):
        if not rate:
            return False
        if (150 > rate > -150) or (-150 < rate < 150):
            return False
        return True

    def is_good_mfi_rate(self, rate):
        if not rate:
            return False
        if (65 > rate > 25) or (25 < rate < 65):
            return False
        return True

    def get_result(self):
        result = []

        for symbol in self.symbols:
            print('**************')
            print(symbol)

            time.sleep(15)

            daily_rsi_rate = self.get_daily_rsi_rate(symbol)
            print('Daily RSI rate:', daily_rsi_rate)

            time.sleep(15)

            daily_cci_rate = self.get_daily_cci_rate(symbol)
            print('Daily CCI rate:', daily_cci_rate)

            time.sleep(15)

            daily_mfi_rate = self.get_daily_mfi_rate(symbol)
            print('Daily MFI rate:', daily_mfi_rate)

            good_indicators = 0

            if self.is_good_rsi_rate(daily_rsi_rate):
                good_indicators += 1
            if self.is_good_cci_rate(daily_cci_rate):
                good_indicators += 1
            if self.is_good_mfi_rate(daily_mfi_rate):
                good_indicators += 1

            print('Good Indicators:', good_indicators)

            if (good_indicators >= 2):
                result.append({'symbol': symbol})

        print(result)
        return result
