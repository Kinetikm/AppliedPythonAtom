# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:09:57 2019

@author: User
"""
import json


def read_file(filename, enc):
    try:
        return read_json(filename, enc)
    except UnicodeDecodeError:
        return read_tsv(filename, enc)


def read_json(filename, enc):
    with open(filename, 'r', encoding=enc) as f:
        raw_data = json.load(f, object_pairs_hook=dict, parse_int=str)
    head = raw_data[0]
    headers = head.keys()
    data = [[header] for header in headers]
    for item in raw_data:
        for i, val in enumerate(item.values()):
            data[i].append(val)

    return data


def read_tsv(filename, enc):
    with open(filename, 'r', encoding=enc) as tsv:
        head = tsv.readline()
        headers = head.strip().split('\t')
        n_cols = len(headers)
        data = [[header] for header in headers]
        for line in tsv:
            tmp = line.strip().split('\t')
            for i in range(n_cols):
                data[i].append(tmp[i])
    return data
