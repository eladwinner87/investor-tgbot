import time
from config import Config
from services import telegramAPI, investLogic

TelegramAPI, investLogic = telegramAPI.TelegramAPI, investLogic.investLogic

def bot():
    SESSION_START = int(time.time())
    TelegramAPI.send_message("Hey, it's time for investments📈💵!\nwhat's the salary this month?💰\nTake your time :)")

    while int(time.time()) - SESSION_START < Config.TIMEOUT:
        TIME_ELAPSED = int(time.time()) - SESSION_START
        response = TelegramAPI.retrieve_response()

        if response["timestamp"] > SESSION_START:
            break
        elif int(time.time()) - SESSION_START == Config.WARNING_TIME:
            TelegramAPI.send_message("Turning off soon⏳")
            time.sleep(1)

    if response["timestamp"] > SESSION_START:
        result = investLogic(response["salary"])
        TelegramAPI.send_message(result)
        
        with open(Config.LOG_FILENAME, "w") as f:
           print(result, file=f)
    else:
        TelegramAPI().send_message("Okay see you next month I guess!")

bot()
