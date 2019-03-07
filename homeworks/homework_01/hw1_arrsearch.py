#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    s = set(input_list)
    for i in s:
        diff = n - i
        if diff in s:
            return input_list.index(i), input_list.index(diff)
    return None
    raise NotImplementedError
