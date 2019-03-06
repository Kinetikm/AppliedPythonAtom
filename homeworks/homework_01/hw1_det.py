#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''

    zero = 1e-9
    rows = len(list_of_lists)
    columns = len(list_of_lists[0])

    # check for none
    if rows != columns:
        return "None"

    m = 0
    while m < len(list_of_lists) - 1:
        if len(list_of_lists[m]) != len(list_of_lists[m + 1]):
            return "None"
        m += 1

    # determinant
    det = 1
    for i in range(0, rows):
        k = i
        for j in range(i+1, rows):
            if abs(list_of_lists[j][i]) > abs(list_of_lists[k][i]):
                k = j
        if abs(list_of_lists[k][i]) < zero:
            det = 0
            break
        list_of_lists[i], list_of_lists[k] =\
            list_of_lists[k], list_of_lists[i]
        if i != k:
            det = -det
        det *= list_of_lists[i][i]
        for j in range(i+1, rows):
            list_of_lists[i][j] /= list_of_lists[i][i]
        for j in range(0, rows):
            if j != i and (abs(list_of_lists[j][i]) > zero):
                for k in range(i+1, rows):
                    list_of_lists[j][k] -= list_of_lists[i][k] \
                                           * list_of_lists[j][i]

    return det
