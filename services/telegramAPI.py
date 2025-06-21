import requests
from config import Config

class TelegramAPI:
    BASE_URL = f"https://api.telegram.org/bot{Config.BOT_TOKEN}"
    
    def send_message(self, text):
        return requests.get(
            f"{self.BASE_URL}/sendMessage",
            data={
                "chat_id": Config.CHAT_ID,
                "text": text
            }
        )
    
    def retrieve_response(self):
        base_response = requests.get(f"{self.BASE_URL}/getUpdates?offset=-1").json()["result"][0]["message"]

        response = {}

        response["chat_id"] = int(base_response["chat"]["id"])
        response["timestamp"] = int(base_response["date"])
        response["salary"] = int(base_response["text"])

        return response