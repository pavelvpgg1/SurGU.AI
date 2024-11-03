import asyncio
import logging
from email.message import Message

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from pyexpat.errors import messages

from AI.apiGigaChat import UseAI

from dotenv import load_dotenv

settings = load_dotenv()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot_token = Bot(token="7696658425:AAFUmZxrEOskasUXn0XG-ZGrc9EurAXPvP0")
AI_token = UseAI().get_token()

# Диспетчер
dp = Dispatcher()
dct_users = {}


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Я твой личный психолог! Обращайся ко мне по любому вопросу! "
                         "Если вдруг решишь закончить диалог на определенную тему, то пропиши команду /delete_history")


@dp.message(Command("delete_history"))
async def cmd_delete_history(message: types.Message):
    if str(message.from_user.id) in dct_users:
        dct_users[str(message.from_user.id)] = []  # Удаляем историю сообщений пользователя
        await message.answer("История сообщений успешно удалена✅")
    else:
        await message.answer("У вас нет сохраненной истории сообщений❌")


@dp.message()
async def any_message(message: types.Message):
    await message.answer("Сообщение принято, готовим ответ...⌛")
    if str(message.from_user.id) not in dct_users:
        dct_users[str(message.from_user.id)] = [message.text]
    else:
        dct_users[str(message.from_user.id)] += [message.text]
    answer = UseAI().get_answer(dct_users.get(str(message.from_user.id)), AI_token)
    await message.answer(answer)
    dct_users[str(message.from_user.id)] += [answer]
    print(dct_users)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot_token)


if __name__ == "__main__":
    asyncio.run(main())
