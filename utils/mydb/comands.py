import logging
import math
import os
import sys

from datetime import datetime
from typing import Optional

from loader import db
from utils.web_scrapper.NewsScrapper import fill_news_table


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def add_user(user_id, phone, first_n, last_n) -> None:
    """ Додає користувача до MySQL """
    async with db.connection.cursor() as cursor:
        await cursor.execute(f"INSERT INTO users (user_id, phone, first_name, last_name)"
                             f"VALUES ({user_id}, {phone}, '{first_n}', '{last_n}')"
                             f"ON DUPLICATE KEY UPDATE user_id=user_id")
        logging.info("User " + str(user_id) + " added to table")


async def get_users():
    """ Повертає усіх користувачів """
    async with db.connection.cursor() as cursor:
        user_table = await cursor.fetch("SELECT * FROM users")
    return user_table


async def get_new_blog() -> str:
    """ Перевіряє дані з ресурсу на наявність нового допису """
    with open(os.path.join(sys.path[0], "utils/mydb/database_init/news_table.sql"), "r") as file:
        sql = file.read()
    async with db.connection.cursor() as cursor:
        await cursor.execute("DROP TABLE news")
        await cursor.execute(sql)

        await fill_news_table()
        await cursor.execute("SELECT title, link, date_post FROM news WHERE id = 1")
        news_table = await cursor.fetchall()

    for blog in news_table:
        if str(blog[2]) == datetime.today().strftime('%Y-%m-%d'):
            logging.info("Find new post " + blog[1])
            return f"{blog[0]}<a href = \"{blog[1]}\"> " + " ➡️" + " </a>\n"


async def get_news_page(page: int) -> Optional[str]:
    """ Формує вивід для однієї сторінки дописів """
    async with db.connection.cursor() as cursor:
        await cursor.execute(f"SELECT id, title, link, date_post FROM news ORDER BY date_post DESC")
        news_table = await cursor.fetchall()
    out = '<b>📩 Новини:</b>\n\n'
    # logging.info("Pages " + str(page))

    if page == 0:
        first_elem = 0
        last_elem = 5
    elif 0 < page <= math.ceil((len(news_table) / 5)):
        counter = page * 5
        first_elem = 0 + counter
        last_elem = 5 + counter
    else:
        return

    for i, news_dict in enumerate(news_table[first_elem:last_elem]):
        page_num = i + 1 + (page * 5)
        # logging.info(str(news_dict))
        title = news_dict[1]
        link = f"<a href = \"{news_dict[2]}\"> «детальніше»</a>"
        date_post = str(news_dict[3])

        out += f"{page_num}. {title} {link}\n<i>{date_post}</i>\n\n"

    return out
