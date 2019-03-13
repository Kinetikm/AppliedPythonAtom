import json
import csv
import os


def check_tsv(file2):
    finallines = []
    for i in file2:
        if len(i) == 0:
            return False
        finallines.append(i)
    size = len(finallines[0])
    for i in finallines:
        if len(i) != size:
            return False
    return True


def check_encoding(path):
    encoding = ['utf-8', 'utf-16', 'cp1251']
    for enc in encoding:
        try:
            open(path, encoding=enc).read()
        except (UnicodeDecodeError, LookupError, UnicodeError):
            pass
        else:
            return enc


def chech_valid(path):
    if os.path.isfile(path) is False:
        print("Файл не валиден")
        return False
    else:
        try:
            with open(path, encoding=check_encoding(path)) as fl:
                file1 = json.load(fl)
                return 'json'
        except BaseException:
            try:
                with open(path, encoding=check_encoding(path)) as fl:
                    file2 = csv.reader(fl, delimiter='\t')
                    if check_tsv(file2) is False:
                        print('Формат не валиден')
                        return False
                    else:
                        return 'tsv'
            except BaseException:
                print('Формат не валиден')
                return False
