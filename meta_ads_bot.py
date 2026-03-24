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
        "date_preset": "yesterday",
        "level": "account",
        "fields": "spend,impressions,reach,clicks,cpc,cpm,ctr"
    }
    resp = requests.get(url, params=params).json()
    
    if "data" in resp:
        data = resp["data"][0]
        spend = float(data.get("spend", 0))
        impressions = int(data.get("impressions", 0))
        reach = int(data.get("reach", 0))
        clicks = int(data.get("clicks", 0))
        cpc = float(data.get("cpc", 0))
        cpm = float(data.get("cpm", 0))
        ctr = float(data.get("ctr", 0)) * 100  # % format
        
        report = f"""
🔔 <b>META ADS YESTERDAY</b>
<i>act_3635946859955819</i>

💰 <b>Spend:</b> {spend:,.0f}đ
👁️ <b>Impressions:</b> {impressions:,}
🌐 <b>Reach:</b> {reach:,}
🖱️ <b>Clicks:</b> {clicks:,}
💸 <b>CPC:</b> {cpc:,.0f}đ
📊 <b>CPM:</b> {cpm:,.0f}đ
🎯 <b>CTR:</b> {ctr:.2f}%

✅ Bot hoàn hảo!
{datetime.now().strftime('%H:%M %d/%m')}
        """.strip()
        
        send_telegram(report)
        print("✅ CPM + CTR OK!")
    else:
        print(f"❌ Lỗi: {resp}")

if __name__ == "__main__":
    main()
