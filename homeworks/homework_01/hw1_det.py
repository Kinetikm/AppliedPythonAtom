#!/usr/bin/env python
# coding: utf-8

import copy


def calculate_determinant(list_of_lists):
    m_len = len(list_of_lists)
    n_len = len(list_of_lists[0])
    if m_len != n_len:
        return None
    if n_len == 1:
        return list_of_lists[0][0]
    sign = 1
    det = 0
    for j in range(n_len):
        det += list_of_lists[0][j] * sign * calculate_determinant(
            minor(list_of_lists, 0, j))
        sign *= -1
    return det


def minor(list_of_lists, i, j):
    minor_matrix = copy.deepcopy(list_of_lists)
    del minor_matrix[i]
    for i in range(len(list_of_lists[0]) - 1):
        del minor_matrix[i][j]
    return minor_matrix


'''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
