import datetime
import logging
import math

from loader import db


async def add_user(user_id, phone, first_n, last_n):
    await db.pool.execute("INSERT INTO users (user_id, phone, first_name, last_name)"
                          "VALUES ($1, $2, $3, $4) ON CONFLICT DO NOTHING", user_id, phone, first_n, last_n)
    logging.info("User " + str(user_id) + " added to table")


async def add_blog(title, link, date_post):
    await db.pool.execute("INSERT INTO blog (title, link, date_post)"
                          "VALUES ($1, $2, $3) ON CONFLICT DO NOTHING", title, link,
                          datetime.datetime.strptime(date_post, '%d.%m.%Y'))


async def subscribe_user(status, user_id):
    await db.pool.execute("UPDATE users SET blog = $1 WHERE user_id = $2", status, user_id)


async def get_blog_page(page: int):

    blog_table = await db.pool.fetch("SELECT id, title, link, date_post FROM blog ORDER BY date_post DESC")
    out = '<b>📩 Останні записи нашого блогу:</b>\n\n'
    logging.info("Pages " + str(page))

    if page == 1:
        first_elem = 0
        last_elem = 5
    elif 1 < page <= math.ceil((len(blog_table) / 5)):
        counter = (page - 1) * 5
        first_elem = 0 + counter
        last_elem = 5 + counter
    else:
        logging.info("Last page")
        return

    for blog_dict in blog_table[first_elem:last_elem]:
        out += f"{blog_dict['title']} " \
               f"<a href = \"{blog_dict['link']}\"> " + "➡️" + " </a>\n" \
               f"<i>{str(blog_dict['date_post'])}</i>\n\n"

    return out

