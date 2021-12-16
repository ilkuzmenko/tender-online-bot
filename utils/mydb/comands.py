import logging
import os
import sys

from datetime import datetime

from loader import db
from utils.web_scrapper.NewsScrapper import fill_news_table


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def get_table(sql: str) -> tuple:
    """ Receives all data from table """
    async with db.connection.cursor() as cursor:
        await cursor.execute(sql)
        table = await cursor.fetchall()
    return table


async def get_users() -> tuple:
    """ Повертає усіх користувачів """
    return await get_table("SELECT * FROM users")


async def get_news_sorted() -> tuple:
    """ Повертає усіх користувачів """
    return await get_table("SELECT id, title, link, date_post FROM news ORDER BY date_post DESC")


async def subscription_status(user_id) -> bool:
    """ Checks subscription status """
    async with db.connection.cursor() as cursor:
        await cursor.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
        if bool(await cursor.fetchone()):
            return True
        return False


async def add_user(user_id: int, phone: int, first_n: str, last_n: str) -> None:
    """ Додає користувача до MySQL """
    async with db.connection.cursor() as cursor:
        await cursor.execute(f"INSERT INTO users (user_id, phone, first_name, last_name)"
                             f"VALUES ({user_id}, {phone}, '{first_n}', '{last_n}')"
                             f"ON DUPLICATE KEY UPDATE user_id=user_id")
        logging.info("User " + str(user_id) + " added to table")


async def subscribe_user(user_id: int) -> str:
    """ Subscribes user to the news """
    try:
        async with db.connection.cursor() as cursor:
            await cursor.execute(f"SELECT news FROM users WHERE user_id = {user_id}")
            status = int(''.join(map(str, await cursor.fetchone())))
            if status == 0:
                await cursor.execute(f"UPDATE users SET news = 1 WHERE user_id = {user_id}")
                return "✅ Ви успішно підписалися!"
            else:
                await cursor.execute(f"UPDATE users SET news = 0 WHERE user_id = {user_id}")
                return "❌ Ви успішно відпідписалися!"
    except TypeError:
        return "❌ Схоже Ви не зареєстровані, виконайте команду /start та спробуйте ще!"


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
