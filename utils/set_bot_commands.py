from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запуск бота"),
        types.BotCommand("help", "Допомога"),
        types.BotCommand("mem", "Зроби правильний вибір:)"),
        types.BotCommand("quiz", "Створити вікторину"),
        types.BotCommand("testing", "Перші тести з укр мови"),
        types.BotCommand("start_test", "Рандомні питання")
    ])
