import time, datetime
from config import Config
from services import telegramAPI, investLogic

TelegramAPI, investLogic = telegramAPI.TelegramAPI, investLogic.investLogic

def bot():
    SESSION_START = int(time.time())
    TelegramAPI().send_message("Hey, it's time for investments📈💵!\nwhat's the salary this month?💰\nTake your time :)")

    while int(time.time()) - SESSION_START < Config.TIMEOUT:
        ELAPSED_TIME = int(time.time()) - SESSION_START
        response = TelegramAPI().retrieve_response()

        if response["timestamp"] > SESSION_START:
            break
        elif ELAPSED_TIME == Config.WARNING_TIME:
            TelegramAPI().send_message("Turning off soon⏳")
            time.sleep(1)

    if response["timestamp"] > SESSION_START:
        result = investLogic(response["salary"])
        TelegramAPI().send_message(result)
        
        with open(f"{Config.LOGS_PATH}/investor_summary_{datetime.datetime.now().strftime('%d-%m-%Y')}.txt", "w") as f:
           print(result, file=f)
    else:
        TelegramAPI().send_message("Okay see you next month I guess!")

bot()
