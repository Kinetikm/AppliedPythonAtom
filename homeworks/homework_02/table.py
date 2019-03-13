import sys
import json
import csv
import codecs

# Ваши импорты


class WorkWithFile:
    fn = ''
    enc = ''

    def __init__(self, fn):
        self.fn = fn
        self.check_encoding()

    def parsing(self):
        if self.enc:
            try:
                res = self.try_json()
            except ValueError:
                res = self.try_tsv()
            if not res:
                print("Формат не валиден")
            else:
                return res

    def check_encoding(self):
        encoding_list = ["utf8", "utf16", "cp1251"]
        for enc in encoding_list:
            try:
                f = codecs.open(self.fn, encoding=enc, errors='strict')
                for _ in f:
                    pass
                self.enc = enc
                break
            except UnicodeDecodeError:
                continue
            except UnicodeError:
                continue
            except ValueError:
                continue
            except FileNotFoundError:
                print("Файл не валиден")
                break
        if not enc:
            print("Формат не валиден")

    def try_json(self):
        with open(self.fn, encoding=self.enc) as input_file:
            col_dict = json.load(input_file)
        return col_dict

    def try_tsv(self):
        col_list = []
        with open(self.fn, encoding=self.enc) as input_file:
            line_list = csv.reader(input_file, delimiter="\t")
            for line in line_list:
                col_list.append(line)
            return col_list


class TablePrint:
    input_date = {}
    caption = []
    sizes = []

    def __init__(self, d: list):
        if d:
            self.input_date = d
            if isinstance(d[0], dict):
                self.caption = list(d[0].keys())
            elif isinstance(d[0], list):
                self.caption = d[0]
                self.input_date.pop(0)

    def sizing(self):
        self.sizes = [len(x) for x in self.caption]
        for line in self.input_date:
            i = 0
            for cap in self.caption:
                if isinstance(line, dict):
                    ls = len(str(line[cap]))
                else:
                    ls = len(line[i])
                if ls > self.sizes[i]:
                    self.sizes[i] = ls
                i = i + 1

    def header(self):
        width = sum(self.sizes)+len(self.sizes)*5 + 1
        print(self.hline(width))
        i = 0
        tmp = "|"
        for cap in self.caption:
            tmp = tmp + "  " + cap.center(self.sizes[i]) + "  |"
            i = i + 1
        print(tmp)

    def body(self):
        width = sum(self.sizes) + len(self.sizes) * 5 + 1
        for line in self.input_date:
            i = 0
            tmp = "|"
            for cap in self.caption:
                if isinstance(line, dict):
                    tmp = tmp + "  " + self.justify(line[cap],
                                                    self.sizes[i]) + "  |"
                else:
                    tmp = tmp + "  " + self.justify(line[i],
                                                    self.sizes[i]) + "  |"
                i = i + 1
            if tmp:
                print(tmp)
        print(self.hline(width))

    def hline(self, length: int):
        res = "-"
        return res.center(length, res)

    def justify(self, val: object, width: int):
        if str(val).isnumeric():
            res = str(val).rjust(width)
        else:
            res = str(val).ljust(width)
        return res


if __name__ == '__main__':

    # Ваш код
    a = WorkWithFile("files/posts-cp1251.json")
    b = TablePrint(a.parsing())
    b.sizing()
    b.header()
    b.body()
