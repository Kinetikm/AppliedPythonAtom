import json
import csv


def check_is_exists(f_name):
    try:
        f = open(f_name)
        f.close()
    except FileNotFoundError:
        return False
    return True


def parse_file(f_name, f_format, f_encoding):
    with open(f_name, encoding=f_encoding) as f:
        res_list = []
        if f_format == 'json':
            data = json.load(f)
            res_list.append(list(data[0].keys()))
            for i in range(len(data)):
                res_list.append(list(data[i].values()))
            return res_list
        else:
            reader = csv.reader(f, delimiter="\t")
            for item in reader:
                res_list.append(item)
    return res_list


def print_info(f_name, f_format, f_encoding):
    data = parse_file(f_name, f_format, f_encoding)
    max_lengths = []

    for i in range(len(data[0]) - 1):
        comparing = []
        for j in range(1, len(data)):
            comparing.append(data[j][i])
        max_lengths.append(len(max(comparing,
                                   key=lambda el: 1 if type(el) == int
                                   else len(el))))
    max_lengths.append(len(data[0][-1]))

    print('-'*(sum(max_lengths) - 3)+'-'*len(max_lengths)*8)
    for i in range(len(data)):
        print('|', end='')
        for j in range(len(data[i])):
            print(' ', data[i][j],
                  ' '*(max_lengths[j] - len(str(data[i][j]))), '  |', end='')
        print()
    print('-' * (sum(max_lengths) - 3) + '-' * len(max_lengths) * 8)
    return
