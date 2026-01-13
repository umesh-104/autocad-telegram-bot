import json
import random
import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "YOUR_CHANNEL_ID"

def load_tips():
    with open("autocad_tips.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_random_tip(tips):
    return random.choice(tips)

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text
    }
    requests.post(url, json=payload)

tips = load_tips()
tip = get_random_tip(tips)

message = f"{tip['title']}\n\n{tip['content']}"
send_to_telegram(message)
