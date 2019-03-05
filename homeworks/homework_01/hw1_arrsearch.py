#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    for i in range(len(input_list)):
        if (n - input_list[i]) in input_list:
            return ((input_list.index(input_list[i]), input_list.index(n - input_list[i])))
    else:
        return None