from configparser import ConfigParser

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
