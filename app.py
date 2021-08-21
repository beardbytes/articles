from flask import Flask, request, jsonify, abort
from requests.models import Response
import connect
import ingestion

from elasticsearch.exceptions import RequestError

app = Flask(__name__)
es = connect.connect_elasticsearch()


@app.get('/search')
def search() -> Response:
    try:
        q = request.args.get('q')
        search_obj = {
            "query": {
                "multi_match": {
                    "query": q
                }
            }
        }
        res = es.search(index='articles', doc_type='_doc', body=search_obj)
        return jsonify(res['hits']['hits'])
    except RequestError as e:
        abort(e.status_code, str(e))
    except TypeError as e:
        return jsonify({"error": "unhashable type: 'list'"})


if __name__ == '__main__':
    try:
        url = "https://api.spaceflightnewsapi.net/v3/articles"
        ingestion.create_index(es, 'articles')
        ingestion.store_record(es, 'articles', connect.connect(url))
        app.run(port=5000, debug=True)
    except Exception as e:
        print(str(e))
