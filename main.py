import json
import random
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

def load_tips():
    with open("autocad_tips_1000.json", "r", encoding="utf-8") as f:
        return json.load(f)

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text
    }
    response = requests.post(url, json=payload)
    print("Telegram response:", response.text)

def main():
    tips = load_tips()
    tip = random.choice(tips)
    send_to_telegram(tip["message"])

if __name__ == "__main__":
    main()
