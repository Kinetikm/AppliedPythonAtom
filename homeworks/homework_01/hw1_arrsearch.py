#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    d = {}
    i = 0
    while i < len(input_list):
        d[input_list[i]] = i
        i += 1
    i = 0
    while i < len(input_list):
        j = d.get(n-input_list[i], -1)
        if j != i and j != -1:
            return (i, j)
        i += 1
    return None
    raise NotImplementedError
