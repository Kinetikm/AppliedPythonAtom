# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:39:44 2019

@author: User
"""

def get_full_length(data):
    return [len(max(column, key=len)) for column in data]


def print_it(data):
    lens = get_full_length(data)
    print(lens)
    hyps = '-' * (sum(lens) + (len(lens) - 1) * 5 + 6)
    print(hyps)
    banner = '|  ' + '  |  '.join(column[0].center(col_len)
                                  for column, col_len in zip(data,
                                                             lens)) + '  |'
    print(banner)
    data = [data[i][1:] for i in range(len(data))]
    for i in range(len(data[0])):
        raw = '|  ' + '  |  '.join(column[i].ljust(col_len)
                                   for column, col_len in zip(
            data[:-1], lens)) + '  |  ' + data[-1][i].rjust(lens[-1]) + '  |'
        print(raw)
    print(hyps)