from homeworks.homework_02.tabletask import InvalidFormat

import csv
import json


def __encoding_check(file):
    encodings = ['utf-8', 'utf-16', 'cp1251']
    for code in encodings:
        try:
            with open(file, encoding=code) as f:
                data = f.read(10)
                return code
        except (UnicodeDecodeError, UnicodeError):
            pass
        except FileNotFoundError:
            raise InvalidFormat
    raise InvalidFormat


def get_data_and_type(file):
    code = __encoding_check(file)
    try:
        with open(file, encoding=code) as f:
            data = []
            json_input = json.load(f)
            data.append(list(json_input[0].keys()))
            for value in json_input:
                if list(value.keys()) != data[0]:
                    raise InvalidFormat
                data.append(list(value.values()))
            return "json", data
    except json.decoder.JSONDecodeError:
        pass

    try:
        with open(file, encoding=code) as f:
            data = []
            reader_object = csv.reader(f, delimiter='\t')
            for line in reader_object:
                if len(line) == 0:
                    raise InvalidFormat
                data.append(line)
        return "tsv", data
    except csv.Error:
        raise InvalidFormat
