from aiogram import executor
from handlers import dp
from loader import bot, storage, db
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    await db.create()
    try:

        print("Створюємо таблиці...", end="")
        await db.create_table_with_questions_litra()
        await db.create_table_with_questions_mova()
        await db.create_table_with_questions_for_nagolos()
        print("Готово")
    except Exception as e:
        print(f"\n\nError! {e}")

    print('Бот працює')
    await set_default_commands(dp)


async def on_shutdown(dp):
    await bot.close()
    await storage.close()


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
