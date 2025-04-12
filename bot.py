{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import telebot\
\
API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'\
bot = telebot.TeleBot(API_TOKEN)\
\
@bot.message_handler(commands=['start', 'help'])\
def send_welcome(message):\
    bot.reply_to(message, "\uc0\u55357 \u56395  Welcome to TheMuayThaiTrader Assistant! Type your question or try:\\n- How does the bot work?\\n- How to join?\\n- Paid vs Free")\
\
@bot.message_handler(func=lambda msg: True)\
def handle_message(message):\
    text = message.text.lower()\
\
    if "how does" in text:\
        bot.reply_to(message, "\uc0\u55358 \u56598  The EA monitors Heiken Ashi candles and key levels to auto-trade XAUUSD and forex pairs.")\
    elif "join" in text:\
        bot.reply_to(message, "\uc0\u55357 \u56960  To join, use the affiliate link or pay \'a3199. Full info at themuaythaibot.com")\
    elif "free" in text or "paid" in text:\
        bot.reply_to(message, "\uc0\u55357 \u56504  Free: Join via broker link.\\n\u55357 \u56508  Paid: \'a3199 with any broker.")\
    else:\
        bot.reply_to(message, "\uc0\u10067  I didn't understand that. Try: /help")\
\
bot.infinity_polling()\
}