import json
import logging

from elasticsearch import Elasticsearch


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


def size_of_tenders(user_message):
    elastic = Elasticsearch([{'host': 'localhost', 'port': 9200}], http_auth=("elastic", "changeme"))
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
        logging.info(f"Counts of elastic = {size_res}")
        return size_res


def search_request(user_message, size):
    """ Формує запит та проводить пошук за тендерами Elasticsearch """
    elastic = Elasticsearch([{'host': 'localhost', 'port': 9200}], http_auth=("elastic", "changeme"))
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
        logging.info(f"Counts of elastic = {search_res}")
        return search_res
