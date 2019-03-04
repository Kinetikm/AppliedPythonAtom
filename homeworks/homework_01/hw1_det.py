#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    set_of_len = set()
    for c in list_of_lists:
        set_of_len.add(len(c))
    if len(set_of_len) != 1:
        return None
    if len(list_of_lists) != len(list_of_lists[0]):
        return None

    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists)):
            print(list_of_lists[i][j], end=' ')
        print(' ')
    for i in range(len(list_of_lists) - 1):
        for j in range(i + 1, len(list_of_lists)):
            d = list_of_lists[j][i]
            for k in range(i, len(list_of_lists)):
                list_of_lists[j][k] = list_of_lists[j][k] - d / \
                                      list_of_lists[i][i] * list_of_lists[i][k]

    result = 1
    for i in range(len(list_of_lists)):
        result *= list_of_lists[i][i]
    return result
