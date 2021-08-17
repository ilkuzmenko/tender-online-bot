import logging
import requests

from bs4 import BeautifulSoup
from utils.db.comands import add_blog

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


async def blog_to_db(page_num):

    date_post = []
    title = []
    link = []

    source = requests.get('https://info.tender-online.com.ua/blog/page/' + str(page_num))
    source.encoding = 'utf-8'
    soup = BeautifulSoup(source.text, "html.parser")

    for _link in soup.select('header.entry-header'):
        link.append(_link.a['href'])

    for _title in soup.select('h2'):
        title.append(_title.text.strip())

    for _date_post in soup.select('div.post-date-publish'):
        date_post.append(_date_post.text)

    blogs = list(zip(title, link, date_post))

    logging.info("Zip blogs")

    for column_value in blogs:
        await add_blog(column_value[0], column_value[1], column_value[2])
