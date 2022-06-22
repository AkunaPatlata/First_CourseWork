from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp, db


@dp.message_handler(Command('top_10'), state="*")
async def top_10(message: types.Message):
    score = await db.top_10()
    final_result = '🏆Таблиця рекордів🏆\n' + '\n'.join([f"{i}. {' '.join([record.get('name'),'|', str(record.get('result'))])}"
                                                        for i, record in enumerate(score, start=1)])
    await message.answer(final_result)
