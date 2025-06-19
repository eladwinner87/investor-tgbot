import time, datetime
from config import Config
from services import telegramAPI, investLogic

TelegramAPI, investLogic = telegramAPI.TelegramAPI, investLogic.investLogic

def bot():
    TelegramAPI().send_message("Hey, it's time for investments📈💵!\nwhat's the salary this month?💰\nTake your time :) ")
    session_timestamp = int(time.time())
    response = TelegramAPI().retrieve_response()

    while not response["timestamp"] > session_timestamp and Config.TIMER < Config.TIMEOUT:
        response = TelegramAPI().retrieve_response()

        if Config.TIMER == Config.WARNING_TIME:
            TelegramAPI().send_message("Turning off soon⏳")
        Config.TIMER += 1

    if Config.TIMER < Config.TIMEOUT:
        salary = response["salary"]
        result = investLogic(salary)
        TelegramAPI().send_message(result)
        with open(f"{Config.LOGS_PATH}/investor_summary_{datetime.datetime.now().strftime('%d-%m-%Y')}.txt", "w") as f:
           print(result, file=f)
    else:
        TelegramAPI().send_message("Okay see you next month I guess!")

bot()
