#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    d = {}
    for i in range(len(input_list)):
        d[int(input_list[i])] = i
    for i in range(len(input_list)-1):
        if (n - int(input_list[i])) in d.keys()\
         and d[n-int(input_list[i])] != i:
            return i, d[n - int(input_list[i])]
    return None
