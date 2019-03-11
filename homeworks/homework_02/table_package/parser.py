import json


def try_json(filename, cdc):
    with open(filename, encoding=cdc) as data_file:
        data = json.load(data_file)
    return data
