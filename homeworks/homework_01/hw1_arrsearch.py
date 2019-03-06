#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    list_dict = {}
    for i in range(len(input_list)):
        try:
            list_dict[input_list[i]] = i
        except KeyError:
            continue

    for i in range(len(input_list)):
        found = list_dict.get(n - input_list[i])
        if found is not None:
            if found != i:
                return i, found
            else:
                continue
        else:
            continue
    return None
