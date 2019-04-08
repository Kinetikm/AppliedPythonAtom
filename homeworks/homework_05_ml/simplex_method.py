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
    n, m = np.array(a).shape
    main_matrix = np.zeros((n + 1, n + m + 2))
    main_matrix[:n, :m] = np.array(a)
    main_matrix[-1, :m] = -np.array(c)
    main_matrix[:-1, -1] = np.array(b).T
    main_matrix[:, m:-1] = np.eye(n + 1, n + 1)
    while min(main_matrix[-1, :]) < 0:
        pivot_column = main_matrix[-1, :].argmin()
        pivot_row = (main_matrix[:-1, -1] / main_matrix[:-1,
                                            pivot_column]).argmin()
        main_matrix[pivot_row, :] /= main_matrix[pivot_row, pivot_column]
        for i in range(n + 1):
            if i != pivot_row:
                main_matrix[i, :] -= main_matrix[pivot_row, :] * main_matrix[
                    i, pivot_column]
    index = np.where(main_matrix[:-1, :m] == 1)
    result_x = np.zeros(m, dtype='i4')
    for i in range(len(index[0])):
        result_x[index[1][i]] = main_matrix[index[0][i], -1]
    return result_x


a = np.array([[2, 3, 2], [1, 1, 2]])
b = np.array([1000, 800])
c = np.array([7, 8, 10])

x = simplex_method(a, b, c)
