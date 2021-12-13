import json
import logging

from datetime import datetime
from typing import Optional
from elasticsearch import Elasticsearch
from config import ES_HOST, ES_USER, ES_PASS

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


def search_request(user_message: str, region_name: str) -> Elasticsearch.search:
    """ Формує запит та проводить пошук за тендерами Elasticsearch """

    elastic = Elasticsearch([{'host': ES_HOST, 'port': 9200}], http_auth=(ES_USER, ES_PASS))

    if elastic is not None:
        region_name = region_name if region_name[0] != 'м' else region_name[2:]

        if region_name != "Вся Україна":
            region_object = {
                "bool": {
                    "should": [
                        {"match": {"regions": region_name}}
                    ]
                }
            }
        else:
            region_object = {}

        search_object = {
            "size": 10000,
            "query": {
                "bool": {
                    "must": [
                        {"match": {"title": user_message}},
                        region_object
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

    search_res = search_request(user_message, region)

    if search_res["hits"]["total"] == 0:
        return "Нічого не знайшов 😔"

    answer = ""
    for i in range(search_res["hits"]["total"]):
        tender = search_res["hits"]["hits"][i]
        publishedDate = datetime.strptime(tender["_source"]["publishedDate"][0:10], '%Y-%m-%d').strftime('%d.%m.%Y')
        title = tender["_source"]["title"]
        amount = str(tender["_source"]["amount"])
        currency = tender["_source"]["currency"]
        link = "<a href = \"https://tender-online.com.ua/tender/view/" + str(tender["_id"]) + "\">«детальніше»</a>"
        answer += f"{i+1}. {title}\nОчікування пропозиції\n<i>{publishedDate}</i>\n{amount}{currency}\n{link}\n\n"
    return answer
