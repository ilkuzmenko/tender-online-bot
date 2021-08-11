import asyncio

from loader import bot, create_db
from config import ADMIN_ID


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    await asyncio.sleep(10)
    await create_db()
    await bot.send_message(ADMIN_ID, "Bot on startup")


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
