import csv
from printing import *


def print_tsv(filename, enc):
    s = list()
    with open(filename, encoding=enc) as file:
        sr = csv.reader(file, delimiter="\t")
        for i in sr:
            if len(i) == 0:
                raise ValueError("Формат не валиден")
            s.append(i)
    print_file(s)