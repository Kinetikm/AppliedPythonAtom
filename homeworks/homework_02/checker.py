import json
import csv
import os


def check_encoding(path):
    encodings = ['utf-16', 'utf-8', 'cp1251']
    for i in encodings:
        try:
            open(path, encoding=i).read()
        except (UnicodeDecodeError, LookupError, UnicodeError):
            pass
        else:
            return i


# def check_c(path):
#     correct_encoding = check_encoding(path)
#     with open(path, "r", encoding=correct_encoding) as data:
#         for line in data:
#             if line == '[\n':
#                 return 'json'
#             else:
#                 return 'tsv'


def check_file(file):
    temp = []
    for i in file:
        if len(i) == 0:
            return False
        temp.append(i)
    size = len(temp[0])
    for i in temp:
        if len(i) != size:
            return False
    return True


def check_validation(path):
    if os.path.isfile(path) is False:
        print('Файл не валиден')
        return False
    else:
        encoding = check_encoding(path)
        try:
            with open(path, encoding=encoding) as json_file:
                json_reader = json.load(json_file)
                json_file.close()
                return 'json'
        except BaseException:
            try:
                with open(path, encoding=encoding) as tsv_file:
                    tsv_reader = csv.reader(tsv_file, delimiter="\t")
                    if check_file(tsv_reader) is False:
                        print('Формат не валиден')
                        tsv_file.close()
                        return False
                    else:
                        tsv_file.close()
                        return 'tsv'
            except BaseException:
                print('Формат не валиден')
                tsv_file.close()
                return False


# def check_validation(path, encoding):
#     extention = check_extensions(path)
#     if extention == 'tsv':
#         with open(path, encoding=encoding) as tsv_file:
#             try:
#                 tsv_reader = csv.reader(tsv_file, delimiter="\t")
#                 return True
#             except tsv.decoder.TSVDecodeError:
#                 print('Формат не валиден')
#                 return False
#     else:
#         with open(path, encoding=encoding) as json_file:
#             try:
#                 json_reader = json.load(json_file)
#                 return True
#             except json.decoder.JSONDecodeError:
#                 print('Формат не валиден')
#                 return False
