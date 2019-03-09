import json
import csv


def is_json(filename, encode):
    try:
        with open(filename, encoding=encode) as f:
            json.load(f)
    except json.JSONDecodeError:
        return False
    return True


def is_csv(filename, encode):
    with open(filename, encoding=encode) as f:
        data = csv.reader(f, delimiter="\t")
        length = 0
        for row in data:
            if length != 0 and length != len(row):
                return False
            length = len(row)
    return True


def define_format(filename, encode):
    if is_json(filename, encode):
        return 'json'
    elif is_csv(filename, encode):
        return 'csv'
    else:
        raise SystemExit("Wrong format")
