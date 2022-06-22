from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запуск бота"),
        types.BotCommand("start_lite_ukrlit", "Спробуй себе в 10-ти тестах з літератури!"),
        types.BotCommand("start_lite_mova", "Спробуй себе в 10-ти тестах з мови!"),
        types.BotCommand("start_mix_test", "Пройди тест із 15 питаннь з обох предметів!"),
        types.BotCommand("ukr_mova_themes", "Обери тему яку хочеш дослідити"),
        types.BotCommand("game_test", "Зіграймо в гру"),
        types.BotCommand("top_10", "Таблиця рекордів гри"),
        types.BotCommand("help", "Потрібна допомога? Тицяй сюди"),
        types.BotCommand("advices", "Тут ти зможеш знайти декілька корисних порад для якісної підготовки до ЗНО"),
        types.BotCommand("about_nuwm", "Хочеш дізнатися що таке НУВГП?")
    ])
