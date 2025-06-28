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
        base_response = requests.get(f"{TelegramAPI.BASE_URL}/getUpdates?offset=-1").json()["result"][0]["message"]

        while base_response["date"] <= SESSION_START and int(time.time()) - SESSION_START < TIMEOUT:
            base_response = requests.get(f"{TelegramAPI.BASE_URL}/getUpdates?offset=-1").json()["result"][0]["message"]

            if int(time.time()) - SESSION_START == WARNING:
                TelegramAPI.send_message("Turning off soon⏳")
                time.sleep(1)
    
        response = {}
        response["chat_id"] = int(base_response["chat"]["id"])
        response["timestamp"] = int(base_response["date"])
        response["salary"] = int(base_response["text"])

        if base_response["date"] > SESSION_START:
            response["new"] = True
        else:
            response["new"] = False

        return response