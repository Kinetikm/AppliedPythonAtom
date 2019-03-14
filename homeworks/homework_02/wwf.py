import json
import csv
from .frr import check_encoding


class WorkWithFile:
    fn = ''
    enc = ''

    def __init__(self, fn):
        self.fn = fn
        self.enc = check_encoding(fn)

    def parsing(self):
        if self.enc:
            try:
                res = self.try_json()
            except ValueError:
                res = self.try_tsv()
            if not res:
                print("Формат не валиден1")
            else:
                return res

    def try_json(self):
        with open(self.fn, encoding=self.enc) as input_file:
            col_dict = json.load(input_file)
        return col_dict

    def try_tsv(self):
        length = 0
        col_list = []
        with open(self.fn, encoding=self.enc) as input_file:
            line_list = csv.reader(input_file, delimiter="\t")
            if line_list:
                length = len(line_list[0])
            for line in line_list:
                if len(line) != length:
                    return None
                col_list.append(line)
            return col_list
