from aiogram import types
from loader import dp
from aiogram.dispatcher.filters.builtin import Command


@dp.message_handler(Command('help'), state="*")
async def help_menu(message: types.Message):
    await message.answer(
        "Отже тобі потрібна допомога? Що ж, цей пункт меню саме для цього😁\n\nТисни на одне із цих посиланнь і проходь тести прямо зараз!\n\n"
        "/start_lite_ukrlit - в цих тестах ти зможеш пройти 10 питаннь з української літератури\n"
        "/start_lite_mova - тут ти пройдеш 10 питаннь з української мови\n"
        "/start_mix_test - тут ти пройдеш 15 змішаних тестів\n"
        "/ukr_mova_themes - пройди тести з української мови з вибраної тобою теми\n"
        "/game_test - зіграй в цікаву гру\n"
        "/top_10 - знайди себе та свій результат в таблиці рекордів до гри\n"
        "/advices - отримай декілька порад, щодо підготовки до ЗНО!\n"
        "/about_nuwm - дізнайся про крутий університет, в який ти можеш поступити!")
