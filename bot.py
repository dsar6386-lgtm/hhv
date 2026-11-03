import os
import json
import telebot

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

if not TOKEN:
    raise ValueError("BOT_TOKEN topilmadi!")

if not ADMIN_CHAT_ID:
    raise ValueError("ADMIN_CHAT_ID topilmadi!")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🍔 Sayqal Food ga xush kelibsiz!\n\n"
        "Buyurtma berish uchun pastdagi "
        "🍔 Buyurtma berish tugmasini bosing."
    )


@bot.message_handler(content_types=["web_app_data"])
def receive_order(message):
    try:
        data = json.loads(message.web_app_data.data)

        order_text = (
            "🍔 YANGI SAYQAL FOOD BUYURTMASI!\n\n"
            f"👤 Mijoz: {message.from_user.first_name}\n\n"
            "📦 Buyurtma ma'lumotlari:\n"
            f"{json.dumps(data, ensure_ascii=False, indent=2)}"
        )

        bot.send_message(ADMIN_CHAT_ID, order_text)

        bot.send_message(
            message.chat.id,
            "✅ Buyurtmangiz adminga yuborildi!"
        )

    except Exception as e:
        print("Buyurtma xatosi:", e)
        bot.send_message(
            message.chat.id,
            "Buyurtmani yuborishda xatolik yuz berdi."
        )


bot.infinity_polling()
