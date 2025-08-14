from config import Config
from services.telegramAPI import TelegramAPI
from services.investLogic import investLogic, format_output

def bot():
    TelegramAPI.send_message("Hey, it's time for investments📈💵!\nwhat's the salary this month?💰\nTake your time :)")
    response = TelegramAPI.get_salary()

    if response:
        data = investLogic(response)
        result = format_output(data)
        
        TelegramAPI.send_message(result)
        
        with open(Config.LOG_FILENAME, "w") as f:
           print(result, file=f)
    else:
        TelegramAPI.send_message("Okay see you next month I guess!")

bot()
