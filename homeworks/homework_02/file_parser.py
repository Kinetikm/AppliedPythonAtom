# блок проверки файла json и tsv на соответствие
# формату, получение упорядоченного словаря
import json
from collections import OrderedDict


def parse_json_tsv(filename, encoding):
    try:
        i = 0
        data = []
        format_tsv = True
        file_state = True
        format_json = True
        with open(filename, 'r', encoding=encoding) as f:
            for line in f:
                if (len(line) == 0):
                    format_tsv = False
                    break
                else:
                    lineSplit = line.strip('\n')
                    lineSplit = lineSplit.split('\t')
                    data.append(lineSplit)
                    # print(data[i])
                    if i > 0:
                        if len(data[i - 1]) != len(data[i]):
                            format_tsv = False
                            break
                    i += 1

            if format_tsv is not True:
                f.seek(0)
                try:
                    dataDict = json.load(f, object_pairs_hook=OrderedDict)
                    data = []
                    for i in range(0, len(dataDict)):
                        keysList = []
                        valueList = []
                        for key, value in dataDict[i].items():
                            if type(value) is list:
                                format_json = False
                                break
                            else:
                                # print("key: {}".format(key))
                                keysList.append(key)
                                valueList.append(value)

                        if i == 0:
                            data.append(keysList)

                        list_comp = list(set(keysList) ^ set(data[0]))
                        if len(list_comp) > 0:
                            format_json = False

                        data.append(valueList)
                        # print("dicts: {}".format(dataDict[i]))
                except ValueError as e:
                    format_json = False

    except FileNotFoundError:
        file_state = None
        print('файл не валиден')
    if file_state is True and format_json is True:
        return data
    else:
        return None
