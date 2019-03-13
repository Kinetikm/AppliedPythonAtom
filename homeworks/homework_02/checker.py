import json
import csv


def check_encoding(path):
    encodings = ['utf-16', 'utf-8', 'cp1251']
    for i in encodings:
        try:
            open(path, encoding=i).read()
        except (UnicodeDecodeError, LookupError, UnicodeError):
            pass
        else:
            return i


def check_extensions(path):
    correct_encoding = check_encoding(path)
    with open(path, "r", encoding=correct_encoding) as data:
        for line in data:
            if line == '[\n':
                return 'json'
            else:
                return 'tsv'


def check_validation(path, encoding, extention):
    if extention == 'tsv':
        with open(path, encoding=encoding) as tsv_file:
            try:
                tsv_reader = csv.reader(tsv_file, delimiter="\t")
                return True
            except tsv.decoder.TSVDecodeError:
                print('Формат не валиден')
                return False
    else:
        with open(path, encoding=encoding) as json_file:
            try:
                json_reader = json.load(json_file)
                return True
            except json.decoder.JSONDecodeError:
                print('Формат не валиден')
                return False
