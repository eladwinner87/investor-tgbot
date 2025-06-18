import time, datetime
from config import Config
from utils import telegramAPI, investLogic

TelegramAPI, investLogic = telegramAPI.TelegramAPI, investLogic.investLogic

def bot():
    TelegramAPI().send_message("Hey, it's time for investments📈💵!\nwhat's the salary this month?💰\nTake your time :) ")
    session_timestamp, response_timestamp, i = int(time.time()), int(time.time()), 0

    while not response_timestamp > session_timestamp and i < Config.TIMEOUT:
        response = TelegramAPI().get_updates()
        chat_id = response['result'][0]['message']['chat']['id']
        response_timestamp = response.get("result", [{}])[0].get("message", {}).get("date", "")

        if i == Config.WARNING_TIME:
            TelegramAPI().send_message("Turning off soon⏳")
        i += 1

    if response_timestamp > session_timestamp and chat_id == Config.CHAT_ID:
        salary = int(response.get("result", [{}])[0].get("message", {}).get("text", ""))
        result = investLogic(salary)
        TelegramAPI().send_message(result)
        with open(f"{Config.LOGS_PATH}/investor_summary_{datetime.datetime.now().strftime('%d-%m-%Y')}.txt", "w") as f:
           print(result, file=f)
    else:
        TelegramAPI().send_message("Okay see you next month I guess!")

bot()
