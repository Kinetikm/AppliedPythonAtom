#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    length = len(input_list)
    i = 0
    while i < length:
        j = i+1
        while j < length:
            if input_list[i] + input_list[j] == n:
                a = (i, j)
                return a
            j += 1
        i += 1
    return
