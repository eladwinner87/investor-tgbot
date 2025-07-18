from config import Investor
from .rateConverter import RateConverter

def investLogic(salary: int) -> str:
    toInvest = salary * Investor.TO_INVEST_PERCENTAGE
    output = f"💵 Total to Invest: ILS {toInvest:.2f}\n"

    rate = RateConverter.getExchangeRate() * Investor.EXCHANGE_COMMISSION
    output += f"💲 Blink Rate: {rate:.2f}\n"

    targets = {}

    for target in Investor.USD_TARGETS + Investor.ILS_TARGETS:
        targets[target] = float(toInvest * Investor.RATIOS[f"{target}_PERCENTAGE"])

        if target in Investor.USD_TARGETS:
            targets[target] = targets[target] / rate


    for target in targets:
        if target in Investor.ILS_TARGETS:
            output += f"🇮🇱 {target}: ILS {targets[target]:.2f}\n"
        elif target in Investor.USD_TARGETS:
            output += f"🇺🇸 {target}: ${targets[target]:.2f}\n"

    return output

# 🏦🌍👾🤝