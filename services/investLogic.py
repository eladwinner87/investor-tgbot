from config import Investor, Config
from .rateConverter import RateConverter

def investLogic(salary: int) -> dict:
    data = {}

    data['total_investment'] = float(salary * Investor.TO_INVEST_RATIO)
    data['rate'] = RateConverter.getExchangeRate() * Investor.EXCHANGE_COMMISSION
    data['targets'] = {}

    for target in Investor.USD_TARGETS + Investor.ILS_TARGETS:
        target_amount = data['total_investment'] * Investor.RATIOS[f"{target}_RATIO"]

        if target in Investor.USD_TARGETS:
            target_amount = target_amount / data['rate']
            target_currency = 'USD'
        else:
            target_currency = 'ILS'
        
        data['targets'][target] = {}
        data['targets'][target]['amount'] = target_amount
        data['targets'][target]['currency'] = target_currency
    return data


def format_output(salary: int) -> str:
    data = investLogic(salary)

    output = []

    if Config.ENV == 'dev':
        output.append("===TEST RUN===")

    output.append(f"💵 Total Investment: {data['total_investment']:.2f}")
    output.append(f"💲 Blink Rate: {data['rate']:.2f}")
    output.append("Targets:")

    for target, info in data['targets'].items():
        output.append(f"{target}: {info['amount']:.2f} {info['currency']}")

    return "\n".join(output)
