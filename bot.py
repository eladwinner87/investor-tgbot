import requests
import time, datetime
import os
from dotenv import load_dotenv
from utils.investLogic import investLogic

load_dotenv()

def bot():
    TELEGRAM_API_URL = "https://api.telegram.org/bot"
    token, chatId, logsPath = os.getenv("TG_BOT_TOKEN"), float(os.getenv("CHAT_ID")), os.getenv("LOGS_PATH", "./logs")

    requests.get(f"{TELEGRAM_API_URL}{token}/sendMessage", data={"chat_id": chatId, "text":
        "Hey, it's time for investments📈💵!\nwhat's the salary this month?💰\nTake your time :) "})
    
    session_timestamp, response_timestamp, i = int(time.time()), int(time.time()), 0

    while not response_timestamp > session_timestamp and i < 4000:
        response = requests.get(f"{TELEGRAM_API_URL}{token}/getUpdates?offset=-1").json()
        chat_id = response['result'][0]['message']['chat']['id']
        response_timestamp = response.get("result", [{}])[0].get("message", {}).get("date", "")

        if i == 2700:
            requests.get(f"{TELEGRAM_API_URL}{token}/sendMessage", data={"chat_id": chatId, "text": "Turning off soon⏳"})
        i += 1

    if response_timestamp > session_timestamp and chat_id == chatId:
        salary = float(response.get("result", [{}])[0].get("message", {}).get("text", ""))
        result = investLogic(salary)
        requests.get(f"{TELEGRAM_API_URL}{token}/sendMessage", data={"chat_id": chatId, "text": f"🧮 Calculations for {salary} ILS:\n{result}"})
        with open(f"{logsPath}/investor_sum_{datetime.datetime.now().strftime('%d-%m-%Y')}.txt", "w") as f:
           print(result, file=f)
    else:
        requests.get(f"{TELEGRAM_API_URL}{token}/sendMessage", data={"chat_id": chatId, "text": "Okay see you next month I guess!"})

bot()
