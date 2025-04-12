import telebot
import os

API_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")  # Make sure you set this in Render

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to TheMuayThaiTrader Assistant!\n\nTry:\n- How does the bot work?\n- How to join?\n- Free vs Paid")

@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    text = message.text.lower()

    if "how does" in text:
        bot.reply_to(message, "🤖 The EA monitors conditions on multiple timeframes as well as key levels to auto-trade XAUUSD.")
    elif "join" in text:
        bot.reply_to(message, "🚀 To join, you can use the affiliate link or pay £199. Full info at themuaythaibot.com.")
    elif "free" in text or "paid" in text:
        bot.reply_to(message, "💸 Free: Join via broker link.\n💼 Paid: £199 one-time with any broker.")
    else:
        bot.reply_to(message, "❓ I didn't quite get that. Try 'how does the bot work?' or /help.")

bot.infinity_polling()
