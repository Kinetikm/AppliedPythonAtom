#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    for a in input_list:
        if (n-a) in input_list and input_list.index(a) != input_list.index(n-a):
            return input_list.index(a), input_list.index(n-a)
        if (n-a) in input_list and input_list.index(a) == input_list.index(n-a):
            t = input_list.index(a)
            input_list[t]=[]
            if (n-a) in input_list:
                return t, input_list.index(n-a)
    return None
