import requests
import time
from config import TelegramCreds

class TelegramAPI:
    BASE_URL = f"https://api.telegram.org/bot{TelegramCreds.BOT_TOKEN}"
    
    def send_message(text):
        return requests.get(
            f"{TelegramAPI.BASE_URL}/sendMessage",
            data={
                "chat_id": TelegramCreds.CHAT_ID,
                "text": text
            }
        )
    
    def retrieve_response(TIMEOUT, WARNING):
        SESSION_START = int(time.time())
        response = None
        
        while (
            int(time.time()) - SESSION_START < TIMEOUT and
            (response is None
            or response["chat"]["id"] != TelegramCreds.CHAT_ID
            or response["date"] <= SESSION_START)
            ):

            response = requests.get(f"{TelegramAPI.BASE_URL}/getUpdates?offset=-1").json()["result"][0]["message"]

            if int(time.time()) - SESSION_START == WARNING:
                TelegramAPI.send_message("Turning off soon⏳")
                time.sleep(1)

        if response["date"] > SESSION_START:
            salary = int(response["text"])
            return salary
        else:
            return False