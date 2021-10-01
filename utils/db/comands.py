import logging
import math

from datetime import datetime
from loader import db
from utils.web_scrapper.BlogScrapper import fill_blog_table


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def add_user(user_id, phone, first_n, last_n):
    await db.pool.execute("INSERT INTO users (user_id, phone, first_name, last_name)"
                          "VALUES ($1, $2, $3, $4) ON CONFLICT DO NOTHING",
                          user_id, phone, first_n, last_n)
    logging.info("User " + str(user_id) + " added to table")


async def subscribe_user(status, user_id):
    await db.pool.execute("UPDATE users SET blog = $1 WHERE user_id = $2", status, user_id)


async def get_blog_page(page: int):
    blog_table = await db.pool.fetch("SELECT id, title, link, date_post FROM blog ORDER BY date_post DESC")
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
        link = f"<a href = \"{blog_dict['link']}\"> ➡️</a>"
        title = blog_dict['title']
        date_post = str(blog_dict['date_post'])

        out += f"{page_num}. {title} {link}\n<i>{date_post}</i>\n\n"

    return out


async def get_users():
    user_table = await db.pool.fetch("SELECT * FROM users")
    return user_table


async def get_new_blog():
    await db.pool.execute("DROP TABLE blog")
    await db.create_table("blog_table")
    await fill_blog_table()

    blog_table = await db.pool.fetch("SELECT title, link, date_post FROM blog WHERE id = 1")

    for blog in blog_table:
        if str(blog['date_post']) == datetime.today().strftime('%Y-%m-%d'):
            logging.info("New post " + blog['link'])
            return f"{blog['title']}<a href = \"{blog['link']}\"> " + " ➡️" + " </a>\n"
