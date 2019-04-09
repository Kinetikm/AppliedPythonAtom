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
    result_func_coeffs = {}
    smp_table = np.vstack((a, c*(-1)))
    new_b_col = np.vstack((b, np.array([0]))) #Append a zero to b col
    smp_table = np.hstack((smp_table, np.eye(smp_table.shape[0]), new_b_col))
    while True:
        min_c_elem = np.amin(smp_table[-1])
        if min_c_elem > 0:
            break
        index_of_min_c = np.argmin(smp_table[-1]) #Characteristic column
        min_smp_frac = \
            np.argmin(smp_table[:, -1] / smp_table[:, index_of_min_c])
        tmp_row = smp_table[min_smp_frac]
        tmp_col = smp_table[:, index_of_min_c]
        elem = smp_table[min_smp_frac][index_of_min_c]
        result_func_coeffs[min_smp_frac] = index_of_min_c
        smp_table[:, index_of_min_c] = tmp_row.T
        smp_table[min_smp_frac] = tmp_col.T
        smp_table[min_smp_frac] /= elem
        smp_table[min_smp_frac:index_of_min_c] = elem ** (-1)
        smp_table[:min_smp_frac] -= \
            smp_table[:min_smp_frac, index_of_min_c].reshape(-1, 1) * \
            smp_table[min_smp_frac].reshape(1, -1)
        smp_table[min_smp_frac + 1:] -= \
            smp_table[min_smp_frac + 1:, index_of_min_c].reshape(-1, 1) * \
            smp_table[min_smp_frac].reshape(1, -1)

    x = np.array([None] * a.shape(1))
    for i in range (0, len(x)):
        if i in result_func_coeffs:
            x[i] = smp_table[i, -1]
    return x
