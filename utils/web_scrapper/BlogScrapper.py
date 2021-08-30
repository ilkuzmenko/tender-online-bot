import logging
import requests

from datetime import datetime
from bs4 import BeautifulSoup
from loader import db

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def num_of_pages():

    selected = 0

    source = requests.get('https://info.tender-online.com.ua/blog/')
    source.encoding = 'utf-8'
    soup = BeautifulSoup(source.text, "html.parser")
    soup = soup.select('span.pages')

    for num in soup:
        selected = int(num.text[-2:])
    logging.info("Number of pages = " + str(selected))

    return selected


async def fill_blog_table():

    date_post = []
    title = []
    link = []
    pages = await num_of_pages()

    for page in range(1, pages):
        source = requests.get('https://info.tender-online.com.ua/blog/page/' + str(page))
        source.encoding = 'utf-8'
        soup = BeautifulSoup(source.text, "html.parser")

        for _link in soup.select('header.entry-header'):
            link.append(_link.a['href'])

        for _title in soup.select('h2'):
            title.append(_title.text.strip().replace("’", "")
                         .replace("�", "").replace(" – ", " ")
                         .replace("“", "").replace("”", "")
                         .replace(" № ", " "))

        for _date_post in soup.select('div.post-date-publish'):
            if len(_date_post.text) == 10:
                date_post.append(_date_post.text)
            else:
                date_post.append('01.01.1991')

    blogs = list(zip(title, link, date_post))

    for column_value in blogs:
        logging.info("Add " + str(column_value))
        await db.pool.execute("INSERT INTO blog (title, link, date_post)"
                              "VALUES ($1, $2, $3) ON CONFLICT DO NOTHING", column_value[0], column_value[1],
                              datetime.strptime(column_value[2], '%d.%m.%Y'))
