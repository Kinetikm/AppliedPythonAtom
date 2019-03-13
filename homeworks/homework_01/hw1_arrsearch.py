#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    i = 0
    j = len(input_list) - 1
    while j > 0:
        if input_list[i] + input_list[j] == n:
            return i, j
        elif i < j - 1:
            i = i + 1
        elif j > 1:
            i = 0
            j = j - 1
        else:
            break
    return
