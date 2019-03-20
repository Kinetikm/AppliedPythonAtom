from checker import *
import re


def make_json_table(file_name):
    data = []
    enc = check_encoding(file_name)
    with open(file_name, encoding=enc) as file_name:
        fl = json.load(file_name)
        temp = []
        for i in fl[0].keys():
            temp.append(str(i))
        data.append(temp)
        for line in fl:
            temp = []
            for i in line.values():
                temp.append(str(i))
            data.append(temp)
        file_name.close()
    return data


def make_tsv_table(file_name):
    enc = check_encoding(file_name)
    alllines = []
    with open(file_name, encoding=enc) as fl:
        for line in fl:
            oneline = re.split('\n|\t', line)
            alllines.append(oneline)
        fl.close()
    finallines = []
    for line in alllines:
        templine = []
        for i in line:
            if i != '':
                templine.append(i)
        if templine != []:
            finallines.append(templine)
    return finallines


# def read_file(path, extensions):
#     encoding = check_encoding(path)
#     table = []
#     if extensions == 'tsv':
#         tsv_file = open(path, encoding=encoding)
#         tsv_reader = csv.reader(tsv_file, delimiter="\t")
#         for line in tsv_reader:
#             table.append(line)
#     else:
#         with open(path, encoding=encoding) as json_file:
#             json_reader = json.load(json_file)
#             temp = []
#             for i in json_reader[0].keys():
#                 temp.append(str(i))
#             table.append(temp)
#             for line in json_reader:
#                 temp = []
#                 for i in line.values():
#                     temp.append(str(i))
#                 table.append(temp)
#     return table
