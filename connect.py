import requests
import logging
from elasticsearch import Elasticsearch
import config as conf

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

    def __init__(self, host, port, url) -> None:
        '''
        Parameters
        ----------
        host : str
            The name of the host
        port : int
            The port number
        url : str
            The public api link
        '''
        self.host = host
        self.port = port
        self.url = url

    def connect(self):
        '''
        Returns the connection response to the API

        Raises
        ------
        RequestException
            If the request is not completed
        '''
        try:
            response = requests.get(
                self.url, headers={"accept": "application/json"}).json()
            return response
        except requests.exceptions.RequestException as e:
            raise e

    def connectElasticsearch(self):
        '''
        Returns the connection to ElasticSearch instance

        Prints 
        -------
        'Connection established' if successful else 'Could not connect'
        '''
        _es = None
        _es = Elasticsearch([{'host': self.host, 'port': self.port}])
        if _es.ping():
            print('Connection established to elastic search')
        else:
            print('Could not connect to elastic search')
        return _es

    if __name__ == '__main__':
        '''
        To catch the stack trace
        '''
        logging.basicConfig(level=logging.ERROR)


# the instance of Connect class is created
conn = Connect(conf.host, conf.elastic_port, conf.url)

# the function connectElasticsearch() instance created
es = Connect.connectElasticsearch(conn)

# the function connect() instance created
response = Connect.connect(conn)
