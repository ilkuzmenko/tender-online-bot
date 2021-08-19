import asyncio
import time

from loader import bot
from config import ADMIN
from utils.db.Database import Database
from utils.web_scrapper.BlogScrapper import fill_blog_table


async def on_startup(dp):
    await asyncio.sleep(5)
    db = Database()
    await db.connect()
    await db.create_table("user_table")
    await db.create_table("blog_table")

    start_time = time.time()
    await fill_blog_table()
    await bot.send_message(ADMIN, "Bot on startup")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
