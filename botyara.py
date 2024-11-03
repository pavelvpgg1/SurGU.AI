import asyncio
import logging
from email.message import Message

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from pyexpat.errors import messages

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7696658425:AAFUmZxrEOskasUXn0XG-ZGrc9EurAXPvP0")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет. Я бот")

@dp.message()
async def any_message(message:types.Message):
    await message.answer('kefteme')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())