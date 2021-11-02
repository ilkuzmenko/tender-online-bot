import logging
import math
import os
import sys

from datetime import datetime
from loader import db
from utils.web_scrapper.BlogScrapper import fill_blog_table


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def add_user(user_id, phone, first_n, last_n):
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


async def get_new_blog():
    """ Перевіряє дані з ресурсу на наявність нового допису """
    with open(os.path.join(sys.path[0], "init/blog_table.sql"), "r") as file:
        sql = file.read()
    async with db.connection.cursor() as cursor:
        await cursor.execute("DROP TABLE blog")
        await cursor.execute(sql)

        await fill_blog_table()
        await cursor.execute("SELECT title, link, date_post FROM blog WHERE id = 1")
        blog_table = await cursor.fetchall()

    for blog in blog_table:
        if str(blog[2]) == datetime.today().strftime('%Y-%m-%d'):
            logging.info("Find new post " + blog[1])
            return f"{blog[0]}<a href = \"{blog[1]}\"> " + " ➡️" + " </a>\n"


async def get_blog_page(page: int):
    """ Формує вивід для однієї сторінки дописів """
    async with db.connection.cursor() as cursor:
        await cursor.execute(f"SELECT id, title, link, date_post FROM blog ORDER BY date_post DESC")
        blog_table = await cursor.fetchall()
    out = '<b>📩 Блог:</b>\n\n'
    logging.info("Pages " + str(page))

    if page == 0:
        first_elem = 0
        last_elem = 5
    elif 0 < page <= math.ceil((len(blog_table) / 5)):
        counter = page * 5
        first_elem = 0 + counter
        last_elem = 5 + counter
    else:
        return

    for i, blog_dict in enumerate(blog_table[first_elem:last_elem]):
        page_num = i + 1 + (page * 5)
        print(blog_dict)
        logging.info('#' * 20)
        logging.info(str(blog_dict))
        title = blog_dict[1]
        link = f"<a href = \"{blog_dict[2]}\"> ➡️</a>"
        date_post = str(blog_dict[3])

        out += f"{page_num}. {title} {link}\n<i>{date_post}</i>\n\n"

    return out
