import yaml

# Read config.ini file
with open("web/config.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)

# to get the host, url, index_name, port and file_path of elastic search
elastic_host = data_loaded["ELASTICSEARCH"]['host']
url = data_loaded["ELASTICSEARCH"]['url']
index_name = data_loaded["ELASTICSEARCH"]['index_name']
elastic_port = data_loaded["ELASTICSEARCH"]['port']
file_path = data_loaded["ELASTICSEARCH"]['file_path']

# to get the port, debug and host of flask
flask_port = data_loaded["API"]['port']
debug = data_loaded["API"]['debug']
flask_host = data_loaded["API"]['host']
