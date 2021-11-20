import logging
import requests

from datetime import datetime
from bs4 import BeautifulSoup
from loader import db

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def num_of_pages() -> int:
    """ Рідраховує кількість сторінок на ресурсі info.tender-online.com.ua """
    selected = 0

    source = requests.get('https://info.tender-online.com.ua/blog/')
    source.encoding = 'utf-8'
    soup = BeautifulSoup(source.text, "html.parser")
    soup = soup.select('span.pages')

    for num in soup:
        selected = int(num.text[-2:])
    # logging.info("Number of pages = " + str(selected))

    return selected


async def fill_news_table() -> None:
    """ Збирає дані з ресурсу та наповнює сторінку новин """
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

    news = list(zip(title, link, date_post))
    async with db.connection.cursor() as cursor:
        for column_value in news:
            # logging.info("Add " + str(column_value))
            await cursor.execute(f"INSERT INTO news (title, link, date_post)"
                                 f"VALUES ('{column_value[0]}', '{column_value[1]}',"
                                 f"'{datetime.strptime(column_value[2], '%d.%m.%Y')}')"
                                 f"ON DUPLICATE KEY UPDATE id=id")
