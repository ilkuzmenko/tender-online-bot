import json
import logging
import math
from datetime import datetime
from typing import Optional

from elasticsearch import Elasticsearch
from config import ES_HOST, ES_USER, ES_PASS

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


def size_of_tenders(user_message: str, region: str) -> int:
    """ Формує запит та проводить підрахунок кількості відповідей за тендерами Elasticsearch """
    elastic = Elasticsearch([{'host': ES_HOST, 'port': 9200}], http_auth=(ES_USER, ES_PASS))
    if elastic is not None:
        count_object = {
            "query": {
                "bool": {
                    "must": [
                        {"match": {"title": user_message}},
                        {
                            "bool": {
                                "should": [
                                    {"match": {"regions": region}}
                                ],
                            }
                        }
                    ],
                    "should": [
                        {"match": {"regions": 'Київ'}}
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


def search_request(user_message: str, region: str, size) -> Elasticsearch.search:
    """ Формує запит та проводить пошук за тендерами Elasticsearch """
    elastic = Elasticsearch([{'host': ES_HOST, 'port': 9200}], http_auth=(ES_USER, ES_PASS))
    if elastic is not None:
        search_object = {
            "size": size,
            "query": {
                "bool": {
                    "must": [
                        {"match": {"title": user_message}},
                        {
                            "bool": {
                                "should": [
                                    {"match": {"regions": region}}
                                ],
                            }
                        }
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


async def get_tenders(user_message, region) -> Optional[str]:
    """ Формує вивід однієї сторінки тендерів """
    try:
        size_res = size_of_tenders(user_message, region)
        search_res = search_request(user_message, region, size_res)
        answer = ""

        for i in range(size_res):
            tender = search_res["hits"]["hits"][i]
            publishedDate = datetime.strptime(tender["_source"]["publishedDate"][0:10], '%Y-%m-%d').strftime('%d.%m.%Y')
            title = tender["_source"]["title"]
            amount = str(tender["_source"]["amount"])
            currency = tender["_source"]["currency"]
            link = "<a href = \"https://tender-online.com.ua/tender/view/" + str(tender["_id"]) + "\">«детальніше»</a>"
            answer += f"{i + 1}. {title}\nОчікування пропозиції\n<i>{publishedDate}</i>\n{amount}{currency}\n{link}\n\n"
        return answer
    except IndexError:
        return "Нічого не знайшов 😔"
