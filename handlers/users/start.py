from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=["start"], state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        f'Привіт, {message.from_user.full_name}✌.\nЯ бот, який спробує допомогти тобі підготуватися до ЗНО з української мови та літератури🇺🇦🇺🇦🇺🇦. Обери пункт в меню нижче, щоб почати тестування.',
        reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f'Вибач, я тебе не зрозумів, обери пункт з меню, або клікни на ось це посилання /help',
                        reply_markup=types.ReplyKeyboardRemove())
    print(message)
