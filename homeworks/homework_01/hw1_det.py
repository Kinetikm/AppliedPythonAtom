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

    def rezat(arr, j):
        def func(a):
            return a[:j] + a[j + 1:]

        ar = list(map(func, arr[1:]))
        return ar

    def det(arr):
        d = 0
        if len(arr) != len(arr[0]):
            return None
        if len(arr) == 1:
            return arr[0][0]
        elif len(arr) == 2:
            d += (arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0])
        else:
            one_plus_minus = -1
            i = 0
            for elem in arr[0]:
                one_plus_minus *= -1
                d += one_plus_minus * elem * det(rezat(arr, i))
                i += 1

        return d

    return det(list_of_lists)


print(calculate_determinant([[58.472, 222.501], [-233.389, -47.711]]))
