from config import Investor, Config
from .rateConverter import RateConverter

def investLogic(salary: int) -> dict:
    data = {}

    data['rate'] = RateConverter.getExchangeRate() * Investor.EXCHANGE_COMMISSION
    data['total_investment'] = float(salary * Investor.TO_INVEST_RATIO)
    data['total_stocks'] = 0
    data['targets'] = {}

    for target in Investor.USD_TARGETS + Investor.ILS_TARGETS:
        target_amount = data['total_investment'] * Investor.RATIOS[f"{target}_RATIO"]

        if target in Investor.USD_TARGETS:
            target_amount = target_amount / data['rate']
            data['total_stocks'] += target_amount
            target_currency = 'USD'
            target_flag = '🇺🇸'
        else:
            target_currency = 'ILS'
            target_flag = '🇮🇱'

        data['targets'][target] = {}
        data['targets'][target]['amount'] = target_amount
        data['targets'][target]['currency'] = target_currency
        data['targets'][target]['flag'] = target_flag
    return data


def format_output(salary: int) -> str:
    data = investLogic(salary)

    output = []

    if Config.ENV == 'dev':
        output.append("===TEST RUN===")

    output.append(f"💵 Total Investment: {data['total_investment']:.2f} ILS")
    output.append(f"💲 Blink Rate: {data['rate']:.2f}")
    output.append(f"🏦 Total Stocks: {data['total_stocks']:.2f} USD ({data['total_stocks'] * data['rate']:.2f} ILS)")
    output.append("Targets:")

    for target, info in data['targets'].items():
        output.append(f"{info['flag']} {target}: {info['amount']:.2f} {info['currency']}")

    return "\n".join(output)
