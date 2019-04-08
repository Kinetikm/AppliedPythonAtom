#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
   * https://  https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    num_eq = np.shape(a)[0]
    num_var = np.shape(a)[1]
    c = np.expand_dims(c, axis=0)
    mat = np.concatenate((a, -c), axis=0)
    mat = np.concatenate((mat, np.eye(num_eq+1)), axis=1)
    b = np.append(b, 0)
    b = np.expand_dims(b, axis=1)
    mat = np.concatenate((mat, b), axis=1)
    while np.min(mat[-1, :]) < 0:
        col_ind = np.argmin(mat[-1, :])
        row_ind = np.argmin(mat[:, -1][:-1]/mat[:, col_ind][:-1])
        mat[row_ind, :] = mat[row_ind, :]/mat[row_ind, col_ind]
        for x in range(mat.shape[0]):
            if x == row_ind:
                continue
            else:
                mat[x, :] = -mat[x, col_ind]*mat[row_ind, :] + mat[x, :]
    result = np.zeros(num_var)
    for x in range(num_eq):
        for y in range(num_var):
            if mat[x, y] == 1:
                result[y] = mat[x, -1]
                break
    return result
