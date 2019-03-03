#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    i = 0
    while i < len(list_of_lists):
        if len(list_of_lists[i]) != len(list_of_lists):
            return None
        i += 1
    result = 0
    i = 0
    if len(list_of_lists) == 2:
        return list_of_lists[0][0]*list_of_lists[1][1]-list_of_lists[0][1]*list_of_lists[1][0]
    while i < len(list_of_lists):
        j = 0
        help_list = list_of_lists.copy()
        while j < len(list_of_lists):
            help_list[j] = list_of_lists[j].copy()
            j += 1
        help_list.pop(0)
        j = 0
        while j < len(list_of_lists) - 1:
            help_list[j].pop(i)
            j += 1
        result += (-1)**i*list_of_lists[0][i]*calculate_determinant(help_list)
        i += 1
    return result
    raise NotImplementedError

