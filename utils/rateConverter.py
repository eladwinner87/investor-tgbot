import os
from config import Config

def getExchangeRate():
    match Config.ENV:
        case 'dev':
            response = {'success': True, 'timestamp': 1748966344, 'base': 'EUR', 'date': '2025-06-03', 'rates': {'USD': 1.137132, 'ILS': 4.002764}}
        case _:
            response = requests.get(Config.API_URL, params={
                "access_key": Config.API_KEY,
                "symbols": "USD,ILS",
            }).json()

    realRate = response['rates']['ILS'] / response['rates']['USD']
    return realRate * 1.014204545454545