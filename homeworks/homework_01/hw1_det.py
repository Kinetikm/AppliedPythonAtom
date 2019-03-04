#!/usr/bin/env python
# coding: utf-8
import copy


def calculate_minor(a, i, j):
    minor = copy.deepcopy(a)
    del minor[i]
    for i in range(len(a[0]) - 1):
        del minor[i][j]
    return minor


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    n = len(list_of_lists[0])
    m = len(list_of_lists)
    if m != n:
        return None
    for i in range(1, len(list_of_lists)):
        if m != len(list_of_lists[i]):
            return None
    if n == 1:
        return list_of_lists[0][0]
    determinant = 0
    k = 1
    for i in range(n):
        determinant += list_of_lists[0][i] * calculate_determinant(calculate_minor(list_of_lists, 0, i)) * k
        k *= -1
    return determinant



