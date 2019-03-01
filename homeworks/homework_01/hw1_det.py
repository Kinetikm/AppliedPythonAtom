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
    return det([i for i in range(n)], [i for i in range(n)], list_of_lists)


def det(x, y, A):
    if len(x) == 1:
        return A[x[0]][y[0]]
    ans = 0
    next_y = y[1:]
    for i in range(len(x)):
        next_x = x[::]
        next_x.remove(x[i])
        ans += (-1) ** (i % 2) * A[x[i]][y[0]] * det(next_x, next_y, A)
    return ans
