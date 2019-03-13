import json
import csv


def enc(filename):
    encoding = ['utf-8', 'utf-16', 'cp1251']
    for code in encoding:
        try:
            open(filename, encoding=code).read()
            return code
        except (UnicodeDecodeError, UnicodeError):
            pass
    raise SystemExit


def format(filename, code):
    try:
        with open(filename, encoding=code) as file:
            x = json.load(file)
        return 'json'
    except json.decoder.JSONDecodeError:
        pass
    with open(filename, encoding=code) as file:
        x = csv.reader(file, delimiter='\t')
        length = -1
        for row in x:
            if (len(row) != length and length != -1):
                raise SystemExit
            length = len(row)
    return 'tsv'
