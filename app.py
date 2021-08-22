import config as conf
from flask import Flask, request, jsonify, abort
from requests.models import Response
import connect as conn
from ingestion import Injetion as I

from elasticsearch.exceptions import RequestError


# instance of Flask created
app = Flask(__name__)


@app.get('/search')  # HTTP method 'GET' is invoked with endpoint /search
def search() -> Response:
    '''
    Return JSON list when the endpoint with the query is given

    Example
        http://localhost:5000/search?q=<query>

    Raises
    ------
    RequestError
        If the query is not provided to the url
    '''
    try:
        # to get the query
        q = request.args.get('q')
        # the query to be searched
        search_obj = {
            "query": {
                "multi_match": {
                    "query": q
                }
            }
        }
        # search API of elastic search is used
        res = conn.es.search(index=conf.index_name,
                             doc_type='_doc', body=search_obj)
        return jsonify(res['hits']['hits'])
    except RequestError as e:
        abort(e.status_code, str(e))


if __name__ == '__main__':
    # the instance of Injetion class is created and used to call the methods from the ingestion.py module
    inj = I(conn.es, conf.index_name, conn.response)
    I.createIndex(inj)
    I.storeRecord(inj)
    try:
        # the flask app is running on 5000 port with debuffing is true
        app.run(port=conf.flask_port, debug=conf.debug)
    except RuntimeError as e:
        pass
