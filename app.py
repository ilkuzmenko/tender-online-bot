import asyncio
import logging
import os
import time

from utils.scheduler import scheduler
from utils.mydb.Database import Database
from utils.notifyer import message_to_admins
from utils.web_scrapper.NewsScrapper import fill_news_table

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def on_startup(dp):
    start_time = time.time()
    asyncio.create_task(scheduler())

    db = Database()
    await db.connect()

    await fill_news_table()

    await message_to_admins("Bot on startup")

    logging.info("Bot on startup --- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    path_log_file = 'logfile'

    if not os.path.isfile(path_log_file):
        with open(path_log_file, 'w') as file:
            file.write('Bot launched!')
        try:
            executor.start_polling(dp, on_startup=on_startup)
        finally:
            os.remove(path_log_file)
    else:
        logging.info("Bot launched now. Finishing processes. Goodbye!")


