import config as conf
from flask import Flask, request, jsonify, abort
from requests.models import Response
import connect as conn

from elasticsearch.exceptions import RequestError, ConnectionError, NotFoundError

# instance of Flask created
app = Flask(__name__)


# HTTP method 'GET' is invoked with endpoint /search
@app.route('/search', methods=["GET"])
def search() -> Response:
    '''
    Return JSON list when the endpoint with the query is given

    Example
        http://localhost:5000/search?q=<query>

    Raises
    ------
    RequestError
        If the query is not provided to the url
    ConnectionError
        If the connection to elastic search is interrupted
    NotFoundError
        If the index is not found in elastic search
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
    except ConnectionError as e:
        return jsonify({"error": "Connection Interrupted"},), e.status_code
    except NotFoundError as e:
        abort(e.status_code, str(e))


if __name__ == '__main__':
    if conn.es:
        # the flask app is running on 5000 port with debugging set to true
        app.run(port=conf.flask_port, debug=conf.debug, host=conf.flask_host)
    else:
        pass
