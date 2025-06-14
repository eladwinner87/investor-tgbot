import requests
from config import Config

class TelegramAPI:
    BASE_URL = f"https://api.telegram.org/bot{Config.BOT_TOKEN}"
    
    def send_message(self, text: str):
        return requests.get(
            f"{self.BASE_URL}/sendMessage",
            data={"chat_id": Config.CHAT_ID, "text": text}
        )
    
    def get_updates(self):
        return requests.get(f"{self.BASE_URL}/getUpdates?offset=-1").json()