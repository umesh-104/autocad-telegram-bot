import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
AI_API_KEY = os.getenv("AI_API_KEY")

def generate_tip():
    prompt = """
    Generate ONE AutoCAD tip for beginners.
    Include:
    - Command name
    - Shortcut
    - When to use
    - Steps
    Max 120 words.
    """
    # AI call here
    return "Generated tip text"

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

tip = generate_tip()
send_to_telegram(tip)
