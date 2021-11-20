import json
import logging
import math
from datetime import datetime

from elasticsearch import Elasticsearch
from config import ES_HOST, ES_USER, ES_PASS

# logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
#                     level=logging.INFO)


def size_of_tenders(user_message):
    """ Формує запит та проводить підрахунок кількості відповідей за тендерами Elasticsearch """
    elastic = Elasticsearch([{'host': ES_HOST, 'port': 9200}], http_auth=(ES_USER, ES_PASS))
    if elastic is not None:
        count_object = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"title": user_message}}
                    ],
                    "filter": [
                        {"term": {"status": "active"}},
                        {"range": {"publishedDate": {"lte": "now"}}}
                    ]
                }
            },
        }
        size_res = elastic.count(index='tenders', body=json.dumps(count_object))['count']
        # logging.info(f"Counts of elastic = {size_res}")
        return size_res


def search_request(user_message, size):
    """ Формує запит та проводить пошук за тендерами Elasticsearch """
    elastic = Elasticsearch([{'host': ES_HOST, 'port': 9200}], http_auth=(ES_USER, ES_PASS))
    if elastic is not None:

        search_object = {
            "size": size,
            "query": {
                "bool": {
                    "must": [
                        {"match": {"title": user_message}}
                    ],
                    "filter": [
                        {"term": {"status": "active"}},
                        {"range": {"publishedDate": {"lte": "now"}}}
                    ]
                }
            },
            "sort": [
                {"publishedDate": {"order": "desc"}}
            ]
        }
        search_res = elastic.search(index='tenders', body=json.dumps(search_object))
        # logging.info(f"Counts of elastic = {search_res}")
        return search_res


async def get_tender_page(user_message, page: int):
    """ Формує вивід однієї сторінки тендерів """
    try:
        # logging.info("---------------------")
        # logging.info(user_message)
        # logging.info("---------------------")
        size_res = size_of_tenders(user_message)
        search_res = search_request(user_message, size_res)
        answer = ""

        if page == 0:
            first_elem = 0
            last_elem = 5
        elif 0 < page <= math.ceil((size_res / 5)):
            counter = page * 5
            first_elem = 0 + counter
            last_elem = 5 + counter
        else:
            return

        for i in range(first_elem, last_elem):
            tender = search_res["hits"]["hits"][i]
            link = "<a href = \"https://tender-online.com.ua/tender/view/" + str(tender["_id"]) + "\"> «детальніше»</a>"
            publishedDate = datetime.strptime(tender["_source"]["publishedDate"][0:10], '%Y-%m-%d').strftime('%d.%m.%Y')
            title = tender["_source"]["title"]
            amount = str(tender["_source"]["amount"])
            currency = tender["_source"]["currency"]
            answer += f"{i + 1}. {title}{link}\nОчікування пропозиції\n<i>{publishedDate}</i>\n{amount}{currency}\n\n"
        return answer
    except IndexError:
        return "Нічого не знайшов 😔"
