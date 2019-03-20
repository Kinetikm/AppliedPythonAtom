#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv


def r_tsv(filename, encoding):
    data = []
    with open(filename, encoding=encoding) as file:
        blank = csv.reader(file, delimiter="\t")
        for x in blank:
            data.append(x)
    return data
