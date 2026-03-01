import os
import requests
from datetime import datetime
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("8667593751:AAGLoc_CF4GPmmODBcjDsJLMu6nIMA7NS2M")

coins = {
    "Bitcoin": "BTCUSDT",
    "Ethereum": "ETHUSDT",
    "Binancecoin": "BNBUSDT",
    "Solana": "SOLUSDT",
    "Litecoin": "LTCUSDT",
    "Toncoin": "TONUSDT",
    "Tron": "TRXUSDT",
    "Dogecoin": "DOGEUSDT"
}

def fetch_price(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, timeout=5)
        data = response.json()
        return float(data['price'])
    except:
        return None

def build_message():
    lines = []
    now = datetime.now().strftime("%H:%M")
    lines.append(f"🟢 Alpha (hour: {now})\n")

    for name, symbol in coins.items():
        price = fetch_price(symbol)
        if price:
            lines.append(f"{name:12}: ${price:,.2f}")
        else:
            lines.append(f"{name:12}: N/A")

    return "\n".join(lines)

async def alpha(update, context):
    await update.message.reply_text(build_message())

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("alpha", alpha))

app.run_polling()
