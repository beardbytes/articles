from elasticsearch.exceptions import ConnectionError as ElasticConnectionError
import requests
import logging
from elasticsearch import Elasticsearch
import config as conf
from ingestion import Injetion

import warnings
warnings.filterwarnings("ignore")


class Connect:
    '''
    A class to establish connection to the public api and ElasticSearch

    ....

    Methods
    -------
    connect()
        Establishes a connection to public api (https://api.spaceflightnewsapi.net/v3/articles)

    connectElasticsearch()
        Establihes a connection to elastic search instance
    '''

    def __init__(self) -> None:
        pass

    def connect(self, url):
        '''
        Returns the connection response from the API

        Parameters
        ----------
        url : str
            The public api link

        Raises
        ------
        RequestException
            If the request is not completed
        '''
        try:
            response = requests.get(
                url, headers={"accept": "application/json"}).json()
            return response
        except requests.exceptions.RequestException as e:
            raise e

    def connectElasticsearch(self, host, port):
        '''
        Returns the connection to ElasticSearch instance

        Parameters
        ----------
        host : str
            The name of the host
        port : int
            The port number

        Prints 
        -------
        'Connection established' if successful else 'Could not connect'
        '''
        _es = None
        while True:
            try:
                _es = Elasticsearch([{'host': host, 'port': port}])
                connected = _es.ping()
                if connected:
                    print('Connection established to elastic search')
                else:
                    print("Not connected")
                    break
                return _es
            except ElasticConnectionError as e:
                raise e


            # the instance of Connect class is created
conn = Connect()

# the function connectElasticsearch() instance created
es = Connect.connectElasticsearch(conn, conf.host, conf.elastic_port)

# the function connect() instance created
response = Connect.connect(conn, conf.url)

# the instance of Injetion class is created and used to call the methods from the ingestion.py module
if es:
    inj = Injetion(es, conf.index_name)
    Injetion.createIndex(inj)
    Injetion.storeRecord(inj, response)
