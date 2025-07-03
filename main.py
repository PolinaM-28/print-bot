
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton("📋 Прайс"))
kb.add(KeyboardButton("🚚 Условия доставки"))
kb.add(KeyboardButton("💬 Написать в WhatsApp"))
kb.add(KeyboardButton("💬 Написать в Telegram"))
kb.add(KeyboardButton("👥 Наше сообщество"))

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я помогу тебе с заказом печати 📄\n\n"
        "Выбери интересующий пункт в меню ниже 👇",
        reply_markup=kb
    )

@dp.message_handler(lambda message: message.text == "📋 Прайс")
async def price_handler(message: types.Message):
    await message.answer(
        "📋 *Прайс услуг:*\n\n"
        "🖨️ 1 стр. ч/б печати — 10 ₽\n"
        "🔄 Двусторонняя ч/б печать — 15 ₽\n"
        "📄 Ксерокопия — 15 ₽\n"
        "🕳️ Пробивка (за каждые 30 стр.) — 10 ₽\n"
        "📁 Упаковка в файлик — *Бесплатно*",
        parse_mode='Markdown'
    )

@dp.message_handler(lambda message: message.text == "🚚 Условия доставки")
async def delivery_handler(message: types.Message):
    await message.answer(
        "🚚 *Условия доставки:*\n\n"
        "📦 *Самовывоз* — бесплатно\n"
        "🕖 *После 19:00* — бесплатно\n"
        "⚡ *Экспресс-доставка* (в течение часа) — 250 ₽",
        parse_mode='Markdown'
    )

@dp.message_handler(lambda message: message.text == "💬 Написать в WhatsApp")
async def whatsapp_handler(message: types.Message):
    link = "https://wa.me/79996146303?text=Здравствуйте!%20Хочу%20сделать%20заказ%20на%20печать."
    await message.answer(f"💬 Нажмите, чтобы связаться через WhatsApp:\n{link}")

@dp.message_handler(lambda message: message.text == "💬 Написать в Telegram")
async def telegram_handler(message: types.Message):
    await message.answer("💬 Нажмите, чтобы написать нам в Telegram:\n@print_contact_bot")

@dp.message_handler(lambda message: message.text == "👥 Наше сообщество")
async def group_handler(message: types.Message):
    await message.answer("👥 Присоединяйтесь к нашему сообществу:\nhttps://t.me/+iz2geLDyB-pmMWIy")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
