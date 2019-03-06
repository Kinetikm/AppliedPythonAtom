#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    for a in input_list:
        if (n-a) in input_list:
            return input_list.index(a),\
                    input_list.index(n-a)
        else:
            return None
    return None
