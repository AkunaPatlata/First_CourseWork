from aiogram import types
from loader import dp
from aiogram.dispatcher.filters.builtin import Command

@dp.message_handler(Command('help'))
async def help_menu(message: types.Message):
    await message.answer("Отже тобі потрібна допомога? Що ж, цей пункт меню саме для цього😁\n\nТисни на одне із цих посиланнь і проходь тести прямо зараз!\n\n"
                         "/start_lite_ukrlit - в цих тестах ти зможеш пройти 10 питаннь з української літератури\n"
                         "/start_lite_mova - тут ти пройдеш 10 питаннь з української мови\n"
                         "/start_mix_test - пройди 15 змішаних тестів з української мови та літератури\n"
                         "/try_hard_test - цей тест для тих, хто бажає дізнатися наскільки його нерви є стійкими та перевірити чи є ти насправді готовим до ЗНО😏")