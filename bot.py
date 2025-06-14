import requests
import time, datetime
from utils.telegramAPI import TelegramAPI
from utils.investLogic import investLogic
from config import Config

def bot():
    token, chatId, logsPath = Config.BOT_TOKEN, Config.CHAT_ID, Config.LOGS_PATH

    TelegramAPI().send_message("Hey, it's time for investments📈💵!\nwhat's the salary this month?💰\nTake your time :) ")

    session_timestamp, response_timestamp, i = int(time.time()), int(time.time()), 0

    while not response_timestamp > session_timestamp and i < Config.TIMEOUT:
        response = TelegramAPI().get_updates()
        chat_id = response['result'][0]['message']['chat']['id']
        response_timestamp = response.get("result", [{}])[0].get("message", {}).get("date", "")

        if i == Config.WARNING_TIME:
            requests.get(f"{TELEGRAM_API_URL}{token}/sendMessage", data={"chat_id": chatId, "text": "Turning off soon⏳"})
        i += 1

    if response_timestamp > session_timestamp and chat_id == chatId:
        salary = int(response.get("result", [{}])[0].get("message", {}).get("text", ""))
        result = investLogic(salary)
        TelegramAPI().send_message(f"🧮 Calculations for {salary} ILS:\n{result}")
        with open(f"{logsPath}/investor_sum_{datetime.datetime.now().strftime('%d-%m-%Y')}.txt", "w") as f:
           print(result, file=f)
    else:
        TelegramAPI().send_message("Okay see you next month I guess!")

bot()
