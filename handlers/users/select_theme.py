from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp


@dp.message_handler(Command("ukr_mova_themes"), state="*")
async def themes_menu(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text="Наголос", callback_data='nagolos'),
            InlineKeyboardButton(text="Апостроф", callback_data='apostrof')
        ],
        [
            InlineKeyboardButton(text="Подвоєння літер", callback_data='double_letters'),
            InlineKeyboardButton(text="Складні слова", callback_data='skladni')
        ],
        [
            InlineKeyboardButton(text="Правопис префіксів", callback_data='prefiks')
        ],
        [
            InlineKeyboardButton(text="Написання слів іншомовного походження", callback_data='foreign')
        ]
    ])
    await message.answer("💫Обери тему з української мови зі списку нижче, з якої хочеш пройти тести💫",
                         reply_markup=keyboard)
