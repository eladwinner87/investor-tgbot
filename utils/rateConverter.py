from config import Config
import requests

class RateConverter:
    def fetchLiveRate():
        return requests.get(Config.API_URL, params={
                "access_key": Config.API_KEY,
                "symbols": "USD,ILS",
                }).json()

    EXAMPLE_RESPONSE = {'success': True, 'timestamp': 1748966344, 'base': 'EUR', 'date': '2025-06-03', 'rates': {'USD': 1.137132, 'ILS': 4.002764}}

def getExchangeRate():
    match Config.ENV:
        case 'dev':
            response = RateConverter.EXAMPLE_RESPONSE
        case _:
            response = RateConverter.fetchLiveRate()

    realRate = response['rates']['ILS'] / response['rates']['USD']
    return realRate * Config.EXCHANGE_COMMISSION