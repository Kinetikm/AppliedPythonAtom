#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    di = dict()
    for ind1 in range(len(input_list)):
        if input_list[ind1] in di:
            ind2 = di[input_list[ind1]]
            return ind1, ind2
        else:
            di[n-input_list[ind1]] = ind1
    return None

