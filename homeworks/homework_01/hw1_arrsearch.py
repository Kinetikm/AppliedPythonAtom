#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    a = []
    for i in range(len(input_list)):
        a.append(n-input_list[i])
        if input_list[i] in a:
            if a.index(input_list[i]) != i:
                return (a.index(input_list[i]), i)
    return None
    raise NotImplementedError
