import json
from collections import OrderedDict


def parse_json_tsv(filename, encoding):
    try:
        index = 0
        data = []
        tsv_format = True
        file_state = True
        json_format = True
        with open(filename, 'r', encoding=encoding) as file:
            for line in file:
                if len(line) != 0:
                    split_line = line.strip('\n')
                    split_line = split_line.split('\t')
                    data.append(split_line)
                    if index > 0:
                        if len(data[index - 1]) != len(data[index]):
                            tsv_format = False
                            break
                    index += 1
                else:
                    tsv_format = False
                    break

            if tsv_format is not True:
                file.seek(0)
                try:
                    data_dict = json.load(file, object_pairs_hook=OrderedDict)
                    data = []
                    for i in range(0, len(data_dict)):
                        key_list = []
                        value_list = []
                        for key, value in data_dict[i].items():
                            if type(value) is list:
                                json_format = False
                                break
                            else:
                                key_list.append(key)
                                value_list.append(value)

                        if i == 0:
                            data.append(key_list)

                        list_comp = list(set(key_list) ^ set(data[0]))
                        if len(list_comp) > 0:
                            json_format = False

                        data.append(value_list)
                except ValueError:
                    json_format = False

    except FileNotFoundError:
        file_state = None
        print('файл не валиден')
    if file_state is True and json_format is True:
        return data
    else:
        return None
