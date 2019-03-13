import csv
from file_worker import print_table


def parse_csv(f_name, f_encoding):
    with open(f_name, encoding=f_encoding) as f:
        reader = csv.reader(f, delimiter="\t")
        res_list = []
        length = 0
        for item in reader:
            if len(item) == 0:
                raise ValueError
            if length != 0 and len(item) != length:
                raise ValueError
            length = len(item)
            res_list.append(item)
    print_table(res_list)
