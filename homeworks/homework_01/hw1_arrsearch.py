#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    b = ()
    for i in range(len(input_list)):
        j = 0
        while j < i:
            if (input_list[j]+input_list[i]) == n:
                b = (j, i)
            j = j + 1
    if b == ():
        return None
    return b
    raise NotImplementedError
