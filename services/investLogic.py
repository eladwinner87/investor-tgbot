from config import Investor
from .rateConverter import RateConverter

def investLogic(salary: int) -> dict:
    raw_data = {}

    raw_data['total_investment'] = float(salary * Investor.TO_INVEST_PERCENTAGE)
    raw_data['rate'] = RateConverter.getExchangeRate() * Investor.EXCHANGE_COMMISSION
    raw_data['targets'] = {}

    for target in Investor.USD_TARGETS + Investor.ILS_TARGETS:
        target_amount = raw_data['total_investment'] * Investor.RATIOS[f"{target}_PERCENTAGE"]

        if target in Investor.USD_TARGETS:
            target_amount = target_amount / raw_data['rate']
            target_currency = 'USD'
        else:
            target_currency = 'ILS'
        

        raw_data['targets'][target] = {}

        raw_data['targets'][target]['amount'] = target_amount
        raw_data['targets'][target]['currency'] = target_currency
    return raw_data


def format_output(data: dict) -> str:

    output = []
    output.append(f"Total Investment: {data['total_investment']:.2f}")
    output.append(f"Exchange Rate: {data['rate']:.2f}")
    output.append("Targets:")

    for target, info in data['targets'].items():
        output.append(f"{target}: {info['amount']:.2f} {info['currency']}")

    return "\n".join(output)

# 🏦🌍👾🤝