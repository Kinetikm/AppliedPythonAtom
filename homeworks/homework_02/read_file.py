import json
import csv


def read_file(path, encoding, extensions):
    table = []
    if extensions == 'tsv':
        tsv_file = open(path, encoding=encoding)
        tsv_reader = csv.reader(tsv_file, delimiter="\t")
        for line in tsv_reader:
            table.append(line)
    else:
        with open(path, encoding=encoding) as json_file:
            json_reader = json.load(json_file)
            temp = []
            for i in json_reader[0].keys():
                temp.append(str(i))
            table.append(temp)
            for line in json_reader:
                temp = []
                for i in line.values():
                    temp.append(str(i))
                table.append(temp)
    return table
