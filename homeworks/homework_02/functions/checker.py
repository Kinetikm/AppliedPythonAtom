import json
import csv


def define_enc(filename):
    for enc in ['utf8', 'utf16', 'cp1251']:
        try:
            with open(filename, 'r', encoding=enc) as f:
                f.readline()
            return enc
        except UnicodeError:
            continue
    # если все-таки не определился enc
    raise UnicodeError


def is_json(filename):
    try:
        enc = defineEnc(filename)
        with open(filename, "r", encoding=enc) as f:
            data = json.load(f)
        if len(data) == 0:
            raise ValueError
        return True
    except json.JSONDecodeError:
        return False


def is_tsv(filename):
    enc = define_enc(filename)
    with open(filename, "r", encoding=enc) as f:
        # data = csv.reader(f, delimiter='\t')
        data = []
        for row in list(csv.DictReader(f, dialect='excel-tab')):
            data.append(row)
    if len(data) == 0:
        raise ValueError
    return True


def define_format(filename):
    if is_json(filename):
        return 0
    elif is_tsv(filename):
        return 1
    else:
        raise UnicodeDecodeError


def is_valid_data(dd):
    # проверка, что одинаковое число столбцов
    if not all([len(d) == len(dd[0]) for d in dd]):
        raise ValueError

    # проверка, что одинаковые шапки
    if not all([d.keys() == dd[0].keys() for d in dd]):
        raise ValueError
