import json
from file_worker import print_table


def parse_json(f_name, f_encoding):
    with open(f_name, encoding=f_encoding) as f:
        res_list = []
        data = json.load(f)

        res_list.append(list(data[0].keys()))
        if 'Название' not in list(data[0].keys()):
            raise ValueError
        length = len(list(data[0].keys()))
        for i in range(len(data)):
            if len(list(data[i].values())) != length:
                raise ValueError
            res_list.append(list(data[i].values()))
            length = len(list(data[i].values()))
    print_table(res_list)
