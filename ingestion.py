class Injetion():
    '''
    Class created to inject the data from public api to ElasticSearch

    ...

    Methods
    -------
    createIndex()
        Index created in order to create documnets, which are the key-value pairs

    storeRecord()
        Stores out data in the form of kwy-value pairs in the documnets
    '''

    def __init__(self, es, index_name, response) -> None:
        '''
        Parameters
        ----------
        es : Response
            Elastic Search instance from connect.py module
        index_name : str
            The name of the index
        response : Response
            The instance from connect.py module
        '''
        self.es = es
        self.index_name = index_name
        self.response = response

    def createIndex(self) -> bool:
        '''
        Creates the document structure in the form of key-value pair

        Raises
        ------
        Exception
            If the index created does not conform to the keys present in the incoming data
        '''
        created = False
        # index settings
        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0,
            },
            "mappings": {
                "dynamic": "strict",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "title": {
                        "type": "text"
                    },
                    "url": {
                        "type": "text"
                    },
                    "imageUrl": {
                        "type": "text"
                    },
                    "newsSite": {
                        "type": "text"
                    },
                    "summary": {
                        "type": "text"
                    },
                    "publishedAt": {
                        "type": "date"
                    },
                    "updatedAt": {
                        "type": "date"
                    },
                    "featured": {
                        "type": "boolean"
                    },
                    "launches": {
                        "type": "nested",
                        "properties": {
                            "id": {"type": "text"},
                            "provider": {"type": "text"}
                        }
                    },
                    "events": {
                        "type": "nested",
                        "properties": {
                            "id": {"type": "text"},
                            "provider": {"type": "text"}
                        }
                    },
                }
            }
        }
        try:
            if not self.es.indices.exists(self.index_name):
                self.es.indices.create(index=self.index_name, body=settings)
                print('Created Index')
            created = True
        except Exception as ex:
            print(str(ex))
        finally:
            return created

    def storeRecord(self) -> None:
        '''
        Stores the data into the index created by createIndex() function in the form of key-value pair

        Raises
        ------
        Exception
            If the data type present in the fields does not match the incoming data
        '''
        try:
            for article in self.response:
                _id = article['id']
                self.es.index(
                    index=self.index_name, doc_type='_doc', id=_id, body=article)
        except Exception as ex:
            print('Error in indexing data')
            print(str(ex))

    def searchQuery(es_object, index_name, body):
        pass
