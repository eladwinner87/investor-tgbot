import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = int(os.getenv("CHAT_ID"))
    
    API_URL = os.getenv("API_URL")
    API_KEY = os.getenv("API_KEY")
    
    ENV = os.getenv("ENV", "dev")
    LOGS_PATH = os.getenv("LOGS_PATH", "./logs")
    
    TIMEOUT = 4500
    WARNING_TIME = 3000