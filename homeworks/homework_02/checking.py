import json
import csv


def check_encoding(filename):
    for code in ['utf8', 'utf16', 'cp1251']:
        try:
            with open(filename, 'r', encoding=code) as file:
                file.readline()
            return code
        except UnicodeError:
            continue
    raise UnicodeError


def json_format(filename):
    try:
        code = check_encoding(filename)
        with open(filename, "r", encoding=code) as file:
            data = []
            json_input = json.load(file)
            data.append(list(json_input[0].keys()))
            for value in json_input:
                if list(value.keys()) != data[0]:
                    raise ValueError
                data.append(list(value.values()))
            return True, data
    except json.decoder.JSONDecodeError:
        return False, None


def tsv_format(filename):
    try:
        code = check_encoding(filename)
        with open(filename, "r", encoding=code) as file:
            data = []
            lines = csv.reader(file, delimiter='\t')
            for line in lines:
                data.append(line)
            return True, data
    except csv.Error:
        return False, None
