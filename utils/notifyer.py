import logging
import time

from config import ADMINS
from loader import bot
from utils.db.comands import get_users


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def message_to_all(message_text):
    """ Реалізує розсилку по всім користувачам з PostgreSQL """
    if message_text:
        start_time = time.time()
        users_table = await get_users()

        for user in users_table:
            await bot.send_message(user['user_id'], message_text, parse_mode='HTML')

        logging.info("Messages to all sent --- %s seconds ---" % (time.time() - start_time))


async def message_to_subscribers(message_text):
    """ Реалізує розсилку за підписаниками з PostgreSQL """
    if message_text:
        start_time = time.time()
        users_table = await get_users()

        for user in users_table:
            if user['blog']:
                await bot.send_message(user['user_id'], message_text, parse_mode='HTML')

        logging.info("Messages to all sent --- %s seconds ---" % (time.time() - start_time))


async def message_to_admins(message_text):
    """ Реалізує розсилку по адміністраторах зі змінних оточення """
    if message_text:
        start_time = time.time()
        admins_list = ADMINS.split(", ")

        for admin in range(len(admins_list)):
            await bot.send_message(admins_list[admin], message_text, parse_mode='HTML')

        logging.info("Messages to admins sent --- %s seconds ---" % (time.time() - start_time))
