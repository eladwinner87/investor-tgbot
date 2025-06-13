import requests
import time, datetime
import os
from dotenv import load_dotenv

load_dotenv()

def getExchangeRate():
    API_URL = os.getenv("API_URL")
    API_KEY = os.getenv("API_KEY")

    match os.getenv("ENV"):
        case 'dev':
            response = {'success': True, 'timestamp': 1748966344, 'base': 'EUR', 'date': '2025-06-03', 'rates': {'USD': 1.137132, 'ILS': 4.002764}}
        case _:
            response = requests.get(API_URL, params={
                "access_key": API_KEY,
                "symbols": "USD,ILS",
            }).json()

    realRate = response['rates']['ILS'] / response['rates']['USD']
    return realRate * 1.014204545454545

def investLogic(salary):
    toInvest = salary * 0.65
    rate = getExchangeRate()
    btb = toInvest / 3
    stocksILS = (toInvest - btb)
    stocks = stocksILS / rate
    qqqm = stocks / 3
    acwi = stocks - qqqm
    output = f"💲Blink Rate: {rate:.2f}\n🏦 Total Stocks: ${stocks:.2f} ({stocksILS:.2f} ILS)\n🌍 ACWI: ${acwi:.2f}\n👾 QQQM: ${qqqm:.2f}\n🤝 BTB: {btb:.2f} ILS"
    return output

def bot_session():
    TELEGRAM_API_URL = "https://api.telegram.org/bot"
    token = os.getenv("TG_BOT_TOKEN")
    myChatId = os.getenv("MY_CHAT_ID")
    logsPath = os.getenv("LOGS_PATH", "./logs")

    requests.get(f"{TELEGRAM_API_URL}{token}/sendMessage", data={"chat_id": myChatId, "text":
        "Hey, it's time for investments📈💵!\nwhat's the salary this month?💰\nI'll be here for the next hour :) "})
    
    session_timestamp = int(time.time())

    response_timestamp, i = 0, 0

    while i < 3600 and response_timestamp < session_timestamp:
        user_input = requests.get(f"{TELEGRAM_API_URL}{token}/getUpdates?offset=-1").json()
        chat_id = user_input['result'][0]['message']['chat']['id']
        response_timestamp = user_input.get("result", [{}])[0].get("message", {}).get("date", "")

        if i == 2700:
            requests.get(f"{TELEGRAM_API_URL}{token}/sendMessage", data={"chat_id": myChatId, "text": "Turning off in 15 minutes⏳"})

        i += 1

    if response_timestamp < session_timestamp and chat_id == myChatId:
        requests.get(f"{TELEGRAM_API_URL}{token}/sendMessage", data={"chat_id": myChatId, "text": "Okay see you next month I guess!"})
    else:
        salary = user_input.get("result", [{}])[0].get("message", {}).get("text", "")
        
        result = investLogic(float(salary))
        requests.get(f"{TELEGRAM_API_URL}{token}/sendMessage", data={"chat_id": myChatId, "text": f"🧮 Calculations for {salary} ILS:\n{result}"})
        with open(f"{logsPath}/invest_guide_{datetime.datetime.now().strftime('%d-%m-%Y')}.txt", "w") as f:
           print(result, file=f)

bot_session()
