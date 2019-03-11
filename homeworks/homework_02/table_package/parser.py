import csv
import json


def try_json(filename, cdc):
    with open(filename, encoding=cdc) as data_file:
        data = json.load(data_file)
    return data


def try_tsv(filename, cdc):
    tsv_list = []

    with open(filename, encoding=cdc) as data_file:
        tsvreader = csv.reader(data_file, delimiter="\t")
        for line in tsvreader:
            tsv_list.append(line)
        return tsv_list
