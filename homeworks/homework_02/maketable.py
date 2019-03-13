from checker import *
import re


def make_json_table(file_name):
    data = []
    enc = check_encoding(file_name)
    with open(file_name, encoding=enc) as fl:
        fl = json.load(fl)
        temp = []
        for i in fl[0].keys():
            temp.append(str(i))
        data.append(temp)
        for line in fl:
            temp = []
            for i in line.values():
                temp.append(str(i))
            data.append(temp)
    return data


def make_tsv_table(file_name):
    enc = check_encoding(file_name)
    alllines = []
    with open(file_name, encoding=enc) as fl:
        for line in fl:
            oneline = re.split('\n|\t', line)
            alllines.append(oneline)
    finallines = []
    for line in alllines:
        templine = []
        for i in line:
            if i != '':
                templine.append(i)
        if templine != []:
            finallines.append(templine)
    return finallines
