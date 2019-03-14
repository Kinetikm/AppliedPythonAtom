import json
import csv


def print_table_data(data_source):
    _list = list()
    for i in range(len(data_source[0])):
        maximum = 0
        for j in data_source:
            if type(j[i]) is str and len(str(j[i])) >= maximum:
                maximum = len(str(j[i]))
        _list.append(maximum)
    print("-" * (sum(_list) + (len(data_source[0])-1) * 5 + 6))
    for i in data_source:
        g = 0
        for j in i:
            if data_source.index(i) == 0:
                print("|  " + " " * ((_list[g] - len(str(j)))//2) +
                      str(j) + " " * ((_list[g] - len(str(j)))//2), end="  ")
            else:
                if str(j).isdigit():
                    print("|  " + " " * (_list[g] - len(str(j))) +
                          str(j), end="  ")
                else:
                    print("|  " + str(j) + " " * (_list[g] - len(str(j))),
                          end="  ")
            g += 1
        print("|")
    print("-" * (sum(_list) + (len(data_source[0])-1) * 5 + 6))


def take_data(file_type, file_name, encode):
    if file_type == 'json':
        with open(file_name, encoding=encode) as f:
            data = json.load(f)
            try:
                _list = [list(data[0].keys())]
                for i in data:
                    _list.append(list(i.values()))
            except (KeyError, IndexError):
                raise SystemExit("Формат не валиден")
            print_table_data(_list)
    elif file_type == 'tsv':
        with open(file_name, encoding=encode) as f:
            data = csv.reader(f, delimiter='\t', quotechar="'")
            data = [i for i in data]
            if len(data) < 1:
                raise SystemExit("Формат не валиден")
            print_table_data(data)
