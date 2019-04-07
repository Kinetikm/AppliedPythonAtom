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
    n, m = a.shape

    a_big = np.vstack((a, np.negative(c)))
    a_big = np.hstack((a_big, np.eye(a_big.shape[0])))
    a_big = np.hstack((a_big, np.append(b, [0]).reshape((n+1, 1))))

    # буферный список для индексов res списка по строкам
    row_res_elements = np.array([i for i in range(m, m+n)])
    res = np.zeros(m)

    while np.min(a_big[-1, :-1]) < 0:
        pivot_column_index = np.argmin(a_big[-1, :-1])
        pivot_row_index = np.argmin(((a_big[:, -1] / a_big[:, pivot_column_index])[:-1]))
        pivot_element = a_big[pivot_row_index, pivot_column_index]

        a_big[pivot_row_index] /= pivot_element

        # индексы всех строк, кроме pivot
        row_idxs = [i for i in range(a_big.shape[0]) if i != pivot_row_index]
        for idx in row_idxs:
            buf_element = a_big[idx][pivot_column_index]
            a_big[idx] -= buf_element*a_big[pivot_row_index]

        row_res_elements[pivot_row_index] = pivot_column_index

    for idx1, idx2 in zip(row_res_elements, range(a_big.shape[0])):
        if idx1 < m:
            res[idx1] = a_big[:, -1][idx2]

    return res
