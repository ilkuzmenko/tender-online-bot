import json

from elasticsearch import Elasticsearch

from config import ES_HOST, ES_USER, ES_PASS


def search_request(user_message: str, region_name: str) -> Elasticsearch.search:
    """ Формує запит та проводить пошук за тендерами Elasticsearch """

    elastic = Elasticsearch(
        [{'host': ES_HOST, 'port': 9200}],
        http_auth=(ES_USER, ES_PASS)
    )

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
                        {
                            "bool": {
                                "must_not": [
                                    {"match": {"title": "тестування"}}
                                ]
                            }
                        },
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
        search_res = elastic.search(
            index='tenders',
            body=json.dumps(search_object),
            request_timeout=30
        )
        return search_res
