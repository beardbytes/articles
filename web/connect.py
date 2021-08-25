import requests
from elasticsearch import Elasticsearch

import warnings
warnings.filterwarnings("ignore")


class Connect:
    '''
    A class to establish connection to the public api and ElasticSearch

    -------

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
            _es = Elasticsearch(
                [{'host': host, 'port': port}])
            connected = _es.ping()
            if connected:
                print('Connection established to elastic search')
            else:
                print("Not connected to elastic search")
                break
            return _es
