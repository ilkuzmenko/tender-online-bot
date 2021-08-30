import asyncio
import logging
import time

from utils.scheduler import scheduler
from utils.db.Database import Database
from utils.notifyer import message_to_all, message_to_admins
from utils.web_scrapper.BlogScrapper import fill_blog_table

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def on_startup(dp):
    start_time = time.time()
    asyncio.create_task(scheduler())
    db = Database()

    await asyncio.sleep(0)

    await db.connect()
    await db.create_table("user_table")
    await db.create_table("blog_table")

    await fill_blog_table()

    await message_to_all("Оновлення 1->20152.\nМи оновили функціонал, напишіть /start, щоб  оновлення вступили в силу.")

    await message_to_admins("Bot on startup")

    logging.info("Bot on startup --- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
