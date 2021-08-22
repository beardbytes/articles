from configparser import ConfigParser
from flask import Flask, request, jsonify, abort
from requests.models import Response
from connect import Connect as C
from ingestion import Injetion as I

from elasticsearch.exceptions import RequestError

import warnings
warnings.filterwarnings("ignore")


# instance of Flask created
app = Flask(__name__)

# Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

# Get the port, host, url and index_name of elastic search
elastic_search = config_object["ELASTICSEARCH"]
host = elastic_search["host"]
elastic_port = elastic_search["port"]
url = elastic_search["url"]
index_name = elastic_search["index_name"]

# Get the port number, port and debug of flask
web = config_object["API"]
flask_port = web["port"]
debug = web["debug"]

# the instance of Connect class is created from connect.py module
conn = C(host, elastic_port, url)

# the function connectElasticsearch() instance created, imported from connect.py
es = C.connectElasticsearch(conn)

# the function connect() instance created, imported from connect.py
response = C.connect(conn)


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
        res = es.search(index=index_name,
                        doc_type='_doc', body=search_obj)
        return jsonify(res['hits']['hits'])
    except RequestError as e:
        abort(e.status_code, str(e))


if __name__ == '__main__':
    # the instance of Injetion class is created and used to call the methods from the ingestion.py module
    inj = I(es, index_name, response)
    I.createIndex(inj)
    I.storeRecord(inj)
    try:
        # the flask app is running on 5000 port with debuffing is true
        app.run(port=flask_port, debug=debug)
    except RuntimeError as e:
        pass
