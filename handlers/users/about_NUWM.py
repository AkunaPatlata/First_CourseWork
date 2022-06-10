from aiogram import types
from aiogram.types import ContentType, Message

from loader import dp, bot
from aiogram.dispatcher.filters.builtin import Command


@dp.message_handler(content_types=ContentType.PHOTO)
async def get_photo_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(Command("about_nuwm"))
async def about_NUWM(message: types.Message):
    photo_url = "https://www.education.ua/upload/i/00001815_b.jpg"
    await message.answer("Отже, ти хочеш дізнатися більше про НУВГП? Що ж, ти обрав правильний пункт в меню😄\n"
                         "<b>НУВГП</b> — це сучасні сервіси: безлімітний Google-диск, власний інтернет-магазин «Комора», електронний розклад,електронний деканат, цифровий репозиторій, електронний документообіг, Вікіситет, мобільний додаток «Мій НУВГП», електронний журнал, віртуальне студмістечко, система антиплагіату UNICHECK, навчальна платформа Moodle.\n\n"
                         "Навчання студентів проводиться в 10 навчальних корпусах, де функціонує понад 100 спеціалізованих аудиторій, кабінетів, оснащених сучасною аудіовізуальною апаратурою, комп’ютерною технікою та іншим обладнанням. В університеті діє 15 науково-дослідних лабораторій, серед яких є унікальні: гідравліки, гідротехніки, меліорації і ґрунтознавства, установки водоподачі, водопідготовки та водоочистки тощо.\n\n"
                         "Більше інформації ти зможеш знайти <a href='https://nuwm.edu.ua/'>тут</a>")
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_url, caption="Перший корпус НУВГП")