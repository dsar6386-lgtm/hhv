import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🍔 Sayqal Food ga xush kelibsiz!\n\n"
        "Buyurtma berish uchun menyuni tanlang:\n"
        "/menu — menyuni ko'rish"
    )

@bot.message_handler(commands=["menu"])
def menu(message):
    bot.send_message(
        message.chat.id,
        "🍔 SAYQAL FOOD MENYUSI\n\n"
        "1. Burger\n"
        "2. Lavash\n"
        "3. Hot-dog\n"
        "4. Fri kartoshka\n"
        "5. Ichimlik\n\n"
        "Buyurtma berish uchun admin bilan bog'laning."
    )

bot.infinity_polling()
