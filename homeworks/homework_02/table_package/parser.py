import csv
import json


def try_json(filename, cdc):
    with open(filename, mode='r', encoding=cdc) as data_file:
        data = json.load(data_file)
    return data


def try_tsv(filename, cdc):
    tsv_list = []
    with open(filename, mode='r', encoding=cdc) as data_file:
        for line in csv.reader(data_file, delimiter="\t"):
            tsv_list.append(line)
    return tsv_list
