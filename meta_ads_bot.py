import os
import requests
from datetime import datetime, timedelta

# Config (giữ nguyên)
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
        "fields": "spend,impressions,reach,clicks,cpc,conversations,cost_per_conversation"
    }
    resp = requests.get(url, params=params).json()
    
    if "data" in resp:
        data = resp["data"][0]
        spend = float(data.get("spend", 0))
        impressions = int(data.get("impressions", 0))
        clicks = int(data.get("clicks", 0))
        conversations = int(data.get("conversations", 0))
        cost_per_conv = float(data.get("cost_per_conversation", 0))
        
        report = f"""
🔔 <b>META ADS REPORT</b>

💰 <b>Spend:</b> {spend:,.0f}đ
👁️ <b>Impressions:</b> {impressions:,}
🖱️ <b>Clicks:</b> {clicks:,}

💬 <b>Conversations:</b> {conversations:,}
💸 <b>Cost/Conv:</b> {cost_per_conv:,.0f}đ

🤖 GitHub Bot | {datetime.now().strftime('%d/%m %H:%M UTC')}
        """.strip()
        
        send_telegram(report)
        print("✅ Báo cáo mới (có Conversations) gửi thành công!")
    else:
        print(f"❌ Lỗi: {resp}")

if __name__ == "__main__":
    main()
