#!/usr/bin/env python
# coding: utf-8


import csv
from pechat import *


def print_tsv(filename, enc):
    text = list()
    with open(filename, encoding=enc) as file:
        sr = csv.reader(file, delimiter="\t")
        for i in sr:
            if len(i) == 0:
                raise ValueError("Формат не валиден")
            text.append(i)
    print_file(text)
