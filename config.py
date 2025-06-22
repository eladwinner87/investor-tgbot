import os
import datetime
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENV = os.getenv("ENV", "dev")

    TIMEOUT = int(os.getenv("TIMEOUT"))
    WARNING_TIME = int(os.getenv("WARNING_TIME"))
    
    LOGS_PATH = os.getenv("LOGS_PATH", "./logs")
    LOG_FILENAME = f"{LOGS_PATH}/investor_summary_{datetime.datetime.now().strftime('%d-%m-%Y')}.txt"

class TelegramCreds:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = int(os.getenv("CHAT_ID"))

class RateConverterCreds:
    API_URL = os.getenv("API_URL")
    API_KEY = os.getenv("API_KEY")

class Investor:
    TO_INVEST_PERCENTAGE = float(os.getenv("TO_INVEST_PERCENTAGE"))
    EXCHANGE_COMMISSION = float(os.getenv("EXCHANGE_COMMISSION", 1))

    USD_TARGETS = os.getenv("USD_TARGETS", "").split(",")
    ILS_TARGETS = os.getenv("ILS_TARGETS", "").split(",")

    RATIOS = {}

    for TARGET in USD_TARGETS + ILS_TARGETS:
        RATIOS[f"{TARGET}_PERCENTAGE"] = float(os.getenv(f"{TARGET}_PERCENTAGE"))
