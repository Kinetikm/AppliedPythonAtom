#!/usr/bin/env python
# coding: utf-8


def arrsearch(source_dict):
    if (input_list == None) or (len(input_list) == 0):
        return None
    res = []
    i = 0
    j = len(input_list) - 1
    input_list.sort()
    while (i != j):
        sum = input_list[i] + input_list[j]
        if (sum > n):
            j -= 1
        elif (sum < n):
            i += 1
        else:
            res.append(i)
            res.append(j)
            return tuple(res)
    return None
