from connect import connect, connect_elasticsearch


def create_index(es_object, index_name) -> bool:
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
        if not es_object.indices.exists(index_name):
            # Ignore 400 means to ignore "Index Already Exist" error.
            es_object.indices.create(index=index_name, body=settings)
            print('Created Index')
        created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


def store_record(elastic_object, index_name, response) -> None:
    try:
        for article in response:
            _id = article['id']
            elastic_object.index(
                index=index_name, doc_type='_doc', id=_id, body=article)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))


def search_query(es_object, index_name, body):
    pass


if __name__ == '__main__':
    url = "https://api.spaceflightnewsapi.net/v3/articles"
    response = connect(url)
    es = connect_elasticsearch()
    if es is not None:
        create_index(es, 'articles')
        store_record(es, 'articles', response)
