import requests
import time, datetime

def getBlinkRate():
    API_URL = "http://api.exchangeratesapi.io/v1/latest"
    API_KEY = "3d073799b70cc013a5d1be8ab9b1d631"

    # response = requests.get(API_URL, params={
    #     "access_key": API_KEY,
    #     "symbols": "USD,ILS",
    # }).json()

    response = {'success': True, 'timestamp': 1748966344, 'base': 'EUR', 'date': '2025-06-03', 'rates': {'USD': 1.137132, 'ILS': 4.002764}}

    realRate = response['rates']['ILS'] / response['rates']['USD']
    return realRate * 1.014204545454545

def investLogic(salary):
    toInvest = salary * 0.65
    rate = getBlinkRate()
    btb = toInvest / 3
    stocksILS = (toInvest - btb)
    stocks = stocksILS / rate
    qqqm = stocks / 3
    acwi = stocks - qqqm
    output = f"Blink Rate: {rate:.2f}\nTotal Stocks: ${stocks:.2f} ({stocksILS:.2f} ILS)\nACWI: ${acwi:.2f}\nQQQM: ${qqqm:.2f}\nBTB: {btb:.2f} ILS"
    return output

def bot_session():
    TELEGRAM_API_URL = "https://api.telegram.org/bot"
    TOKEN = "7912633230:AAGtNjdItB-kg6XoaZh0GDIxC2lUVjHJFf8"
    CHAT_ID = "380382224"
    LOGS_PATH = "./logs"

    requests.get(f"{TELEGRAM_API_URL}{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text":
        "Hey, it's time for investments📈💵!"
        "\nwhat's the salary this month?💰"
        "\nI'll be here for the next hour :) "})
    
    session_timestamp = int(time.time())

    response_timestamp, i = 0, 0

    while i < 3600 and response_timestamp < session_timestamp:
        user_input = requests.get(f"{TELEGRAM_API_URL}{TOKEN}/getUpdates?offset=-1").json()
        response_timestamp = user_input.get("result", [{}])[0].get("message", {}).get("date", "")

        if i == 2700:
            requests.get(f"{TELEGRAM_API_URL}{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": "Turning off in 15 minutes⏳"})

        i += 1
    
    if response_timestamp < session_timestamp and user_input['result'][0]['message']['chat']['id'] == CHAT_ID:
        requests.get(f"{TELEGRAM_API_URL}{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": "Okay see you next month I guess!"})
    else:
        salary = user_input.get("result", [{}])[0].get("message", {}).get("text", "")

        result = investLogic(float(salary))
        requests.get(f"{TELEGRAM_API_URL}{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": f"Calculations for {salary} ILS:\n{result}"})
        with open(f"{LOGS_PATH}/invest_guide_{datetime.datetime.now().strftime("%d-%m-%Y")}.txt", "w") as f:
           print(result, file=f)

bot_session()
