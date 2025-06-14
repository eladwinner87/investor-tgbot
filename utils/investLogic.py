from .rateConverter import getExchangeRate

def investLogic(salary):
    toInvest, rate = salary * 0.65, getExchangeRate()
    btb = toInvest / 3
    stocksILS = (toInvest - btb)
    stocks = stocksILS / rate
    qqqm = stocks / 3
    acwi = stocks - qqqm
    output = f"💲Blink Rate: {rate:.2f}\n🏦 Total Stocks: ${stocks:.2f} ({stocksILS:.2f} ILS)\n🌍 ACWI: ${acwi:.2f}\n👾 QQQM: ${qqqm:.2f}\n🤝 BTB: {btb:.2f} ILS"
    return output