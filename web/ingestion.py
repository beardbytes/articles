import json


class Injetion:
    '''
    Class created to inject the data from public api to ElasticSearch

    ...

    Methods
    -------
    createIndex()
        Index created in order to create documents, which are the key-value pairs

    storeRecord()
        Stores the data in the form of key-value pairs in the documents
    '''

    def __init__(self, es, index_name) -> None:
        '''
        Parameters
        ----------
        es : Response
            Elastic Search connection instance
        index_name : str
            The name of the index
        '''
        self.es = es
        self.index_name = index_name

    def createIndex(self, file_path) -> bool:
        '''
        Creates the document structure in the form of key-value pair and returns true if index is created

        Parameter
        ---------
        file_path : str
            the name of the file containing the index

        Raises
        ------
        Exception
            If the index created does not conform to the keys present in the incoming data
        '''
        created = False
        settings = {}
        # json file containing the index settings and fields is loaded
        with open(file_path, 'r') as f:
            data = json.loads(f.read())
        settings = data
        try:
            if not self.es.indices.exists(self.index_name):
                self.es.indices.create(index=self.index_name, body=settings)
                print('Created Index')
            created = True
        except Exception as ex:
            print(str(ex))
        finally:
            return created

    def storeRecord(self, response) -> None:
        '''
        Stores the data into the index created by createIndex() function in the form of key-value pair

        Parameters
        ----------
        response : str
            Data from the API

        Raises
        ------
        Exception
            If the data type present in the fields does not match the incoming data
        '''
        try:
            for article in response:
                _id = article['id']
                self.es.index(
                    index=self.index_name, doc_type='_doc', id=_id, body=article)
        except Exception as ex:
            print('Error in indexing data')
            print(str(ex))
