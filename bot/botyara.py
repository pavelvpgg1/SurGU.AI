import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from AI.apiGigaChat import UseAI

from src.config.project_config import settings


logging.basicConfig(level=logging.INFO)
AI_token = UseAI().get_token()
bot_token = Bot(token=settings.TOKEN)
dp = Dispatcher()
dct_users = {}


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
        dct_users[str(message.from_user.id)] = [f"Ты - психолог-бот в телеграме. Твоя задача помогать людям с их вопросами и переживаниями. А вот это сообщение от пользователя {message.text}"]
    else:
        dct_users[str(message.from_user.id)] += [f"Ты - психолог-бот в телеграме. Твоя задача помогать людям с их вопросами и переживаниями. А вот это сообщение от пользователя {message.text}"]
    answer = UseAI().get_answer(dct_users.get(str(message.from_user.id)), AI_token)
    await message.answer(answer)
    dct_users[str(message.from_user.id)] += [f"{answer} - А вот это уже твой ответ"]
    print(dct_users)


async def main():
    await dp.start_polling(bot_token)


if __name__ == "__main__":
    asyncio.run(main())
