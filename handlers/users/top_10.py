from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.utils.callback_data import CallbackData
import random
from loader import dp, db
from states.states import Test


@dp.message_handler(Command('top_10'), state="*")
async def top_10(message: types.Message):
    score = await db.top_10()
    final_result = '🏆Таблиця рекордів🏆\n' + '\n'.join([f"{i}. {' '.join([record.get('name'),'|', str(record.get('result'))])}"
                                                        for i, record in enumerate(score, start=1)])
    await message.answer(final_result)
