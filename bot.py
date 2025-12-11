from config import Config
from services.telegramAPI import TelegramAPI
from services.investLogic import format_output as process_investments

def bot():    
    TelegramAPI.send_message("Hey, it's time for investments📈💵!\nwhat's the salary this month?💰\nTake your time :)")
    user_salary = TelegramAPI.get_salary()

    if user_salary:
        result = process_investments(user_salary)

        TelegramAPI.send_message(result)
        
        if Config.ENV != 'dev':
            with open(Config.LOG_FILENAME, "w") as f:
                print(result, file=f)

    else:
        TelegramAPI.send_message("Okay see you next month I guess!")

bot()
