#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    if len(input_list) < 2:
        return None

    d = {input_list[0]: 0}
    for i in range(1, len(input_list)):
        diff = n - input_list[i]
        if diff in d.keys():
            return i, d[diff]
        else:
            d[input_list[i]] = i
