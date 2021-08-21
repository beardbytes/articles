import requests
from elasticsearch import Elasticsearch


def connect(url):
    try:
        return requests.get(url, headers={"accept": "application/json"}).json()
    except requests.exceptions.RequestException as e:
        raise e


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Connection established')
    else:
        print('Could not connect')
    return _es
