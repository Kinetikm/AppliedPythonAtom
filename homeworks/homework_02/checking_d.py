import json
import csv


def check_encoding(file):
    for code in ['utf8', 'utf16', 'cp1251']:
        try:
            with open(file, 'r', encoding=code) as f:
                f.readline()

            return code
        except UnicodeError:
            continue
    raise UnicodeError


def true_format(file):
    try:
        code = check_encoding(file)
        with open(file, "r", encoding=code) as f:
            data = []
            json_input = json.load(f)
            data.append(list(json_input[0].keys()))
            for value in json_input:
                if list(value.keys()) != data[0]:
                    raise ValueError
                data.append(list(value.values()))
            # if .json -> 1
            return 1, data
    except json.decoder.JSONDecodeError:
        try:
            code = check_encoding(file)
            with open(file, "r", encoding=code) as f:
                data = []
                lines = csv.reader(f, delimiter='\t')
                for line in lines:
                    data.append(line)
                # if .tsv -> 0
                return 0, data
        except csv.Error:
            # if not .json and not .tsv -> -1
            return -1, None
