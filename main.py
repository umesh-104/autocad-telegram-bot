import os
import requests
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
AI_API_KEY = os.getenv("AI_API_KEY")

client = OpenAI(api_key=AI_API_KEY)

def generate_tip():
    prompt = """
You are a professional AutoCAD trainer.

Generate ONE detailed AutoCAD daily tip.

Rules:
- Beginner-friendly
- Real drafting use-case
- Include:
  • Command name
  • Shortcut key
  • What it is used for
  • Step-by-step usage (numbered)
- Clear formatting
- Max 120 words
- Do NOT mention versions
- Do NOT add emojis
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AutoCAD expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

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
