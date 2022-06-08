from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext


# @dp.message_handler(commands="test4")
# async def with_hidden_link(message: types.Message):
#     await message.answer(
#         f"{fmt.hide_link('https://www.youtube.com/watch?v=M0LeUKmjAQg')}Кто бы мог подумать, что "
#         f"в 2020 году в Telegram появятся видеозвонки!\n\nОбычные голосовые вызовы "
#         f"возникли в Telegram лишь в 2017, заметно позже своих конкурентов. А спустя три года, "
#         f"когда огромное количество людей на планете приучились работать из дома из-за эпидемии "
#         f"коронавируса, команда Павла Дурова не растерялась и сделала качественные "
#         f"видеозвонки на WebRTC!\n\nP.S. а ещё ходят слухи про демонстрацию своего экрана :)",
#         parse_mode=types.ParseMode.HTML)


@dp.message_handler(commands=["start"], state="*")
async def start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        f'Привіт, {message.from_user.full_name}.\n<i>Введи своє повідомлення, яке хочеш зробити капсом. Також бонусом отримай точний поточний час:)</i>',
        reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f'Зараз {str(message.date)[11:]} і твій великий текст:',
                        reply_markup=types.ReplyKeyboardRemove())
    await message.answer(message.text.upper())
    print(message)
