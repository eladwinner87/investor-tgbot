from config import Investor
from .rateConverter import RateConverter

TO_INVEST_PERCENTAGE, EXCHANGE_COMMISSION = Investor.TO_INVEST_PERCENTAGE, Investor.EXCHANGE_COMMISSION
USD_TARGETS, ILS_TARGETS, RATIOS = Investor.USD_TARGETS, Investor.ILS_TARGETS, Investor.RATIOS

def investLogic(salary: int) -> str:
    toInvest = salary * TO_INVEST_PERCENTAGE
    rate = RateConverter.getExchangeRate() * EXCHANGE_COMMISSION

    targets = {}

    for target in USD_TARGETS + ILS_TARGETS:
        targets[target] = float(toInvest * RATIOS[f"{target}_PERCENTAGE"])

        if target in USD_TARGETS:
            targets[target] = targets[target] / rate

    output = f"💰 Investment Breakdown:\n💲 Blink Rate: {rate:.2f}\n"

    for target in targets:
        if target in ILS_TARGETS:
            output += f"🇮🇱 {target}: ILS {targets[target]:.2f}\n"
        elif target in USD_TARGETS:
            output += f"🇺🇸 {target}: ${targets[target]:.2f}\n"

    return output

# 🏦🌍👾🤝