import os
import requests
import telebot
from datetime import datetime

# Variáveis de ambiente do Render
BOT_TOKEN = os.getenv("BOT_TOKEN")
ODDS_API_KEY = os.getenv("ODDS_API_KEY")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(BOT_TOKEN)

ODDS_API_URL = "https://api.the-odds-api.com/v4/sports"
SPORT = "soccer"

def get_matches(min_odds=1.8):
    try:
        url = f"{ODDS_API_URL}?apiKey={ODDS_API_KEY}"
        response = requests.get(url)
        data = response.json()
        matches = []
        for item in data:
            if "bookmakers" in item:
                for book in item["bookmakers"]:
                    for market in book["markets"]:
                        for outcome in market["outcomes"]:
                            if outcome["price"] >= min_odds:
                                matches.append({
                                    "time": item.get("commence_time", ""),
                                    "teams": f"{item['home_team']} x {item['away_team']}",
                                    "odd": outcome["price"]
                                })
        return matches
    except Exception as e:
        return []

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "✅ Bot de palpites iniciado!\nUse /palpites para receber dicas.")

@bot.message_handler(commands=['palpites'])
def send_predictions(message):
    matches = get_matches(min_odds=1.8)
    if not matches:
        bot.reply_to(message, "⚠️ Nenhum palpite encontrado agora.")
        return
    text = "🎯 **Palpites de Hoje**\n\n"
    for m in matches[:5]:  # máximo 5 por vez
        hora = m['time']
        try:
            hora = datetime.fromisoformat(hora.replace("Z", "+00:00")).strftime("%d/%m %H:%M")
        except:
            pass
        text += f"🏆 {m['teams']}\n🕒 {hora}\n💰 Odd: {m['odd']}\n\n"
    bot.reply_to(message, text)

if __name__ == "__main__":
    print("🤖 Bot rodando...")
    bot.infinity_polling()
