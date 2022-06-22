from aiogram import types
from loader import dp


@dp.message_handler(commands=["start"], state="*")
async def start(message: types.Message):
    await message.answer(
        f'Привіт, {message.from_user.full_name}✌.\nЯ бот, який спробує допомогти тобі '
        f'підготуватися до ЗНО з української мови та літератури🇺🇦🇺🇦🇺🇦. '
        f'Обери пункт в меню нижче, щоб почати тестування.',
        reply_markup=types.ReplyKeyboardRemove())
    print(message.from_user.full_name)


@dp.message_handler(text='Привіт')
async def hello(message: types.Message):
    await message.answer(
        "І тобі привіт!👋 Давай проходити тести разом, обери потрібний для тебе пункт в меню і вперед до перемог!💃")


@dp.message_handler(text='привіт')
async def hello(message: types.Message):
    await message.answer(
        "І тобі привіт!👋 Давай проходити тести разом, обери потрібний для тебе пункт в меню і вперед до перемог!💃")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f'Вибач, я тебе не зрозумів, обери пункт з меню, або клікни на ось це посилання /help',
                        reply_markup=types.ReplyKeyboardRemove())
    print(message)
