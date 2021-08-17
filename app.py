import asyncio
import time

from loader import bot, create_user_db, create_blog_db
from config import ADMIN
from utils.web_scrapper.BlogScrapper import blog_to_db


async def on_startup(dp):
    await asyncio.sleep(5)
    await create_user_db()
    await create_blog_db()
    start_time = time.time()
    await blog_to_db(1)
    print("--- %s seconds ---" % (time.time() - start_time))
    await bot.send_message(ADMIN, "Bot on startup")


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
