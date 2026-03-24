import os
import requests
from datetime import datetime, timedelta

BOT_TOKEN = "8603101291:AAGYsIGfCLGcqfby3oUk88ILOFRWMo8X2S4"
CHAT_ID = "2077738684"
AD_ACCOUNT_ID = "act_3635946859955819"
META_TOKEN = os.getenv("META_TOKEN")

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}
    resp = requests.get(url, params=payload)
    print(f"Telegram: {resp.json()}")

def main():
    url = f"https://graph.facebook.com/v20.0/{AD_ACCOUNT_ID}/insights"
    params = {
        "access_token": META_TOKEN,
        "date
