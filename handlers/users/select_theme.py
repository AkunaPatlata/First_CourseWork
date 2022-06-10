from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp


@dp.message_handler(Command("ukr_mova_themes"))
async def themes_menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text="Наголос", callback_data='nagolos'),
            InlineKeyboardButton(text="Апостроф", callback_data='apostrof')
        ]
    ])
    await message.answer("💫Обери тему з української мови зі списку нижче, з якої хочеш пройти тести💫",
                         reply_markup=keyboard)
