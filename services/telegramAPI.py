import requests
import time
from config import Config, TelegramCreds

class TelegramAPI:
    BASE_URL = f"https://api.telegram.org/bot{TelegramCreds.BOT_TOKEN}"
    
    @staticmethod
    def send_message(text):
        return requests.post(
            f"{TelegramAPI.BASE_URL}/sendMessage",
            data={
                "chat_id": TelegramCreds.CHAT_ID,
                "text": text
            }
        )
    
    @staticmethod
    def retrieve_response():
        return requests.get(f"{TelegramAPI.BASE_URL}/getUpdates?offset=-1").json()["result"]

    @staticmethod
    def get_salary():
        SESSION_START = int(time.time())
        response = []
        
        while (
            int(time.time()) - SESSION_START <= Config.TIMEOUT and
            (response == []
            or response[0]["message"]["chat"]["id"] != TelegramCreds.CHAT_ID
            or response[0]["message"]["date"] <= SESSION_START)
            ):

            response = TelegramAPI.retrieve_response()

            if int(time.time()) - SESSION_START == Config.WARNING_TIME:
                TelegramAPI.send_message("Turning off soon⏳")
                time.sleep(1)

        if int(time.time()) - SESSION_START <= Config.TIMEOUT:
            salary = int(response[0]["message"]["text"])
            return salary
        else:
            return False