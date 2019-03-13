import json
import csv


def check_converted_info(converted_info):
    s = ''
    length = -1
    for el in converted_info:
        if (len(el) != length and length != -1):
            raise SystemExit
        length = len(el)
        s += ''.join(str(i) for i in el)
    if len(s) == 0:
        raise SystemExit


def read_json(filename, code):
    converted_info = []
    with open(filename, encoding=code) as filename:
        info = json.load(filename)
        first_row = []
        for name in info[0].keys():
            first_row.append(name)
        for dict_row in info:
            if list(dict_row.keys()) != first_row:
                raise SystemExit
        converted_info.append(first_row)
        for dict_row in info:
            other_rows = [str(x) for x in dict_row.values()]
            converted_info.append(other_rows)
    check_converted_info(converted_info)
    return converted_info


def read_tsv(filename, code):
    converted_info = []
    with open(filename, encoding=code) as filename:
        info = csv.reader(filename, delimiter='\t')
        for x in info:
            converted_info.append(x)
    check_converted_info(converted_info)
    return converted_info


def read_file(filename, code, form):
    if (form == 'json'):
        converted_info = read_json(filename, code)
    else:
        converted_info = read_tsv(filename, code)
    return converted_info