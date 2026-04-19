import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("8592460653:AAEqZdqydZPN2wvqWB-W129Q1RRY-Q5H_h8")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Бот запущен 🚀")

# пример команды
@dp.message(Command("profile"))
async def profile(message: types.Message):
    await message.answer("Профиль работает 👤")

async def main():
    print("Bot started")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())