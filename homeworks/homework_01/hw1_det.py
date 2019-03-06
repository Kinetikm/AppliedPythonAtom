#!/usr/bin/env python
# coding: utf-8
import copy
# list_of_lists = [[1, 4, 3], [4, 5, 6], [7, 8, 9]]


def minor(list_of_list, i, j):
    # print("1: ", list_of_list, i, j)
    mtrx = copy.deepcopy(list_of_list)
    del mtrx[i]
    for i in range(len(list_of_list) - 1):
        del mtrx[i][j]
    return mtrx


def calculate_determinant(list_of_lists):
    # print(list_of_lists)
    column = len(list_of_lists[0])
    row = len(list_of_lists)
    if column != row:
        return None
    if column == 1:
        return list_of_lists[0][0]
    det = 0
    for j in range(column):
        sigma = (-1) ** (2 + j)
        det += list_of_lists[0][j] * sigma *\
            calculate_determinant(minor(list_of_lists, 0, j))
    return det
# print(calculate_determinant(list_of_lists))
# raise NotImplementedError
