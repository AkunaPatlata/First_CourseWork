from aiogram import types
from aiogram.utils.exceptions import BotBlocked
from loader import dp


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    print(f"Користувач мене заблокував!\nПовідомлення: {update}\nПомилка: {exception}")
    return True
