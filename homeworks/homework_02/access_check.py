import json
import csv


def check_json(fd):
    buffer = list()
    try:
        data = json.load(fd)
        buffer.append(list(data[0].keys()))
        for value in data:
            buffer.append(list(value.values()))
    except json.JSONDecodeError:
        fd.seek(0)
        return False
    return buffer


def check_csv(fd):
    B = 0
    buffer = list()
    reader = csv.reader(fd, delimiter="\t")
    for item in reader:
        if not (B == 0 or B == len(item)):
            buffer.clear()
            return False
        B = len(item)
        buffer.append(item)
    return buffer


def check_format(fd):
    buffer_json = check_json(fd)
    buffer_tsv = check_csv(fd)
    if buffer_json:
        return buffer_json
    elif buffer_tsv:
        return buffer_tsv
    else:
        raise Warning
