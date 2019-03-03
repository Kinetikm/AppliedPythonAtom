#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists, res=0):
    if len(list_of_lists) == 0:
        return None
    if len(list_of_lists) == 1:
        if len(list_of_lists[0]) == len(list_of_lists):
            return list_of_lists[0]
        else:
            return None
    pointers = list(range(len(list_of_lists)))
    if len(list_of_lists) == 2:
        if len(list_of_lists[0]) == 2:
            val = list_of_lists[0][0] * list_of_lists[1][1] \
                  - list_of_lists[1][0] * list_of_lists[0][1]
            return val
        else:
            return None
    if len(list_of_lists) != len(list_of_lists[0]):
        return None
    for column in pointers:
        copy_matrix = []
        for item in list_of_lists:
            copy_matrix.append(item.copy())
        copy_matrix = copy_matrix[1:]
        m = len(copy_matrix)
        for i in range(m):
            copy_matrix[i] = copy_matrix[i][0:column] \
                             + copy_matrix[i][column + 1:]
        sign = (-1) ** (column % 2)
        copy_matrix_det = calculate_determinant(copy_matrix)
        res += sign * list_of_lists[0][column] * copy_matrix_det
    return res
    raise NotImplementedError
