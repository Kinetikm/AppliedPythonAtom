#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    input_dict = dict()
    for i in range(len(input_list)):
        if (n - input_list[i]) in input_dict:
            return input_dict[n - input_list[i]], i
        input_dict[input_list[i]] = i
    return None
