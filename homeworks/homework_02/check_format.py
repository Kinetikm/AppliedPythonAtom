import csv
import json


def json_file(file_name, encode):
    try:
        with open(file_name, encoding=encode) as f:
            _data = json.load(f)
    except json.JSONDecodeError:
        return False
    return True


def tsv_file(file_name, encode):
    with open(file_name, encoding=encode) as f:
        _data = csv.reader(f, delimiter='\t')
        _list = list()
        for i in list(_data):
            _list.append(len(i))
        if _list.count(_list[0]) == len(_list):
            return True
        else:
            return False


def check_file_format(file_type, charset):
    if tsv_file(file_type, charset):
        return 'tsv'
    elif json_file(file_type, charset):
        return 'json'
    else:
        raise SystemExit("Формат не валиден")
