import os
import re
import time
import logging
import random
import requests

from urllib.parse import quote_plus
from dotenv import load_dotenv

load_dotenv()  # Load env vars from a .env file if present

# === Configuration ===

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS", "YOUR_CHAT_IDS").split(",")  # comma separated list

QUOTES_FILE = os.getenv("QUOTES_FILE", "quotes.txt")
INDEX_FILE = os.getenv("INDEX_FILE", "current_index.txt")

MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# Emojis to rotate in header
EMOJI_OPTIONS = ["🌟", "🔥", "✨", "💡", "🌈", "⚡"]

# === Setup logging ===

logging.basicConfig(
    filename='telegram_quote_bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# === Functions ===

def load_quotes(filename):
    if not os.path.exists(filename):
        logging.error(f"Quotes file '{filename}' not found.")
        return []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    quotes = [line.strip() for line in lines if line.strip()]
    return quotes

def load_index(filename):
    if not os.path.exists(filename):
        return 0
    with open(filename, "r") as f:
        try:
            return int(f.read().strip())
        except ValueError:
            logging.warning("Invalid index file content. Resetting index to 0.")
            return 0

def save_index(filename, idx):
    with open(filename, "w") as f:
        f.write(str(idx))

def escape_markdown_v2(text):
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    return re.sub(f'([{re.escape(escape_chars)}])', r'\\\1', text)

def send_telegram_message(token, chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "MarkdownV2",
        "disable_web_page_preview": True
    }
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(url, data=payload, timeout=10)
            response.raise_for_status()
            logging.info(f"Message sent to chat_id {chat_id}")
            return True, response.text
        except requests.RequestException as e:
            logging.warning(f"Attempt {attempt} failed for chat_id {chat_id}: {e}")
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY)
            else:
                return False, str(e)

def main():
    quotes = load_quotes(QUOTES_FILE)
    if not quotes:
        logging.error("No quotes found. Exiting.")
        return

    current_index = load_index(INDEX_FILE)
    if current_index >= len(quotes):
        current_index = 0

    quote_raw = quotes[current_index]
    quote_escaped = escape_markdown_v2(quote_raw)

    emoji = random.choice(EMOJI_OPTIONS)
    message = f"{emoji} *Inspiration of the Day:*\n\n_{quote_escaped}_"

    all_success = True
    for chat_id in CHAT_IDS:
        success, response = send_telegram_message(BOT_TOKEN, chat_id.strip(), message)
        if success:
            logging.info(f"Sent quote #{current_index + 1} to chat {chat_id}")
        else:
            logging.error(f"Failed to send quote to chat {chat_id}: {response}")
            all_success = False

    if all_success:
        save_index(INDEX_FILE, current_index + 1)
        logging.info(f"Incremented quote index to {current_index + 1}")
    else:
        logging.warning("Not incrementing index due to send failure.")

if __name__ == "__main__":
    main()
