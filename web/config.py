import yaml

# Read config.ini file
with open("web/config.yaml", 'r') as stream:
    data_loaded = yaml.safe_load(stream)

# for k, v in data_loaded.items():
#     if k == "API":
#         for key, value in data_loaded[k].items():
#             print(value[:])

host = data_loaded["ELASTICSEARCH"]['host']
url = data_loaded["ELASTICSEARCH"]['url']
index_name = data_loaded["ELASTICSEARCH"]['index_name']
elastic_port = data_loaded["ELASTICSEARCH"]['port']

flask_port = data_loaded["API"]['port']
debug = data_loaded["API"]['debug']
# Get the port, host, url and index_name of elastic search
# print(config_object)
# host = elastic_search["host"]
# print(host)
# elastic_port = elastic_search["port"]
# url = elastic_search["url"]
# index_name = elastic_search["index_name"]

# # Get the port number, port and debug of flask
# web = config_object["API"]
# flask_port = web["port"]
# debug = web["debug"]
