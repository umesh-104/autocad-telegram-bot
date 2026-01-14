import json
import random
import requests
import os
import sys

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

print("DEBUG: BOT_TOKEN exists:", bool(BOT_TOKEN))
print("DEBUG: CHANNEL_ID:", CHANNEL_ID)

def load_tips():
    print("DEBUG: Loading JSON file")
    with open("autocad_tips.json", "r", encoding="utf-8") as f:
        tips = json.load(f)
    print("DEBUG: Tips loaded:", len(tips))
    return tips

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text
    }
    response = requests.post(url, json=payload)
    print("DEBUG: Telegram status:", response.status_code)
    print("DEBUG: Telegram response:", response.text)

tips = load_tips()
tip = random.choice(tips)

message = f"{tip['title']}\n\n{tip['content']}"
send_to_telegram(message)
