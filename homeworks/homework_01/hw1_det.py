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
    n = len(list_of_lists)
    for i in list_of_lists:
        if len(i) != n:
            return None
    if n == 1:
        return list_of_lists[0][0]
    if n == 2:
        return list_of_lists[0][0] * list_of_lists[1][1] -\
               list_of_lists[0][1] * list_of_lists[1][0]
    return det([i for i in range(n)], [i for i in range(n)], list_of_lists)


def det(_str, _col, A):
    determ = 0
    t_col = _col[1:]
    for i in range(len(_str)):
        t_str = _str[:]
        t_str.remove(_str[i])
        determ += (-1) ** (i % 2) * A[i][0] * det(t_str, t_col, A)
    return determ
