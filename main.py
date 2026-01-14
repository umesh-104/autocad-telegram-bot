import json
import requests
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

TIPS_FILE = "autocad_tips_1000.json"
INDEX_FILE = "last_index.txt"

def load_tips():
    with open(TIPS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_index():
    if not os.path.exists(INDEX_FILE):
        return 0
    with open(INDEX_FILE, "r") as f:
        return int(f.read().strip())

def save_index(index):
    with open(INDEX_FILE, "w") as f:
        f.write(str(index))

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
    index = load_index()

    if index >= len(tips):
        index = 0  # loop back after 1000

    tip = tips[index]
    send_to_telegram(tip["message"])

    save_index(index + 1)

if __name__ == "__main__":
    main()
