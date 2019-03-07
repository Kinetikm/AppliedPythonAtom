#!/usr/bin/env python
# coding: utf-8


def is_zeros(M, k):
    m, n = -1, -1
    if M[k][k] != 0:
        return 1
    else:
        for i in range(d, len(M)):
            for j in range(d, len(M)):
                if (a[i][j] != 0):
                    m, n = i, j
                    break
        if ((m == -1) and n == -1):
            return 0
        for i in range(len(M)):
            M[k][i], M[m][i] = M[m][i], M[k][i]
        M[k][k], M[k][n] = M[k][n], M[k][k]
        if ((k == m) and (k == n)):
            return 1
        else:
            return -1


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    M = list_of_lists
    if (M is None):
        return None
    n = len(M)
    flag = True
    i, j, k = 0, 0, 1
    for i in range(n):
        if len(M[i]) != n:
            return None
    for i in range(n-1):
        k *= is_zeros(M, i)
        if k == 0:
            return 0
        for j in range(i+1, n):
                c = M[j][i] / M[i][i]
                for p in range(len(M[j])):
                    M[j][p] -= M[i][p] * c
    res = 1
    for i in range(n):
        res *= M[i][i]
    return res * k
    raise NotImplementedError
