import requests
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
    
    def retrieve_response():
        base_response = requests.get(f"{TelegramAPI.BASE_URL}/getUpdates?offset=-1").json()["result"][0]["message"]

        response = {}

        response["chat_id"] = int(base_response["chat"]["id"])
        response["timestamp"] = int(base_response["date"])
        response["salary"] = int(base_response["text"])

        return response