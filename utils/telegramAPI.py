import requests
from config import Config

class TelegramAPI:
    BASE_URL = f"https://api.telegram.org/bot{Config.BOT_TOKEN}"
    
    def send_message(self, text):
        return requests.get(
            f"{self.BASE_URL}/sendMessage",
            data={"chat_id": Config.CHAT_ID, "text": text}
        )
    
    def retrieve_response(self):
        raw_response = requests.get(f"{self.BASE_URL}/getUpdates?offset=-1").json()

        response = {}

        response["chat_id"] = raw_response['result'][0]['message']['chat']['id']
        response["timestamp"] = raw_response.get("result", [{}])[0].get("message", {}).get("date", "")
        response["salary"] = int(raw_response.get("result", [{}])[0].get("message", {}).get("text", ""))

        return response