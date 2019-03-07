#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    hash = {}
    for i in range(len(input_list)):
        hash[int(input_list[i])] = i
    for i in range(len(input_list)):
        if (n - int(input_list[i])) in hash\
         and hash[n - int(input_list[i])] != i:
            return i, hash[n - input_list[i]]
    return None
