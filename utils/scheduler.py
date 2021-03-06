import asyncio
import logging
import aioschedule

from utils.mydb.comands import get_new_news
from utils.notifyer import message_to_subscribers

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def scheduler() -> None:
    """ Ініціалізує та запускає розклад перевірок нових дописів """
    logging.info("Init scheduler: every day at 10:00 GMT")
    aioschedule.every().day.at("10:00").do(blog_message_schedule)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def blog_message_schedule() -> None:
    """ Відпровляє повідомлення з новим дописом """
    await message_to_subscribers(
        await get_new_news()
    )
    logging.info("Blog message sent to users")
