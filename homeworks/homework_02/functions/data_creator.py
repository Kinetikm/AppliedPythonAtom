import json
import csv
from checker import define_enc


def read_json(filename):
    enc = define_enc(filename)
    with open(filename, "r", encoding=enc) as f:
        data = json.load(f)
        print(data)
    return data  # ' '.join([str(elem) for elem in data ]


def read_tsv(filename):
    enc = define_enc(filename)
    with open(filename, "r", encoding=enc) as f:
        # data = csv.reader(f, delimiter='\t')
        data = []
        for row in list(csv.DictReader(f, dialect='excel-tab')):
            data.append(row)
    return data


# привести данные к виду (шапка, данные)
def to_comfort_format(data):
    hat = data[0].keys()
    vals = []
    for dd in data:
        vals.append(list(dd.values()))
    return list(hat), vals
