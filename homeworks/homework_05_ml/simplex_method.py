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
    basis = np.full(len(b), -1)
    table = np.zeros((len(b) + 1, len(a[0]) + len(b) + 2))
    dtable = np.eye(len(b) + 1)
    table[-1, :] = np.hstack([-1*c, dtable[-1], 0])
    for i in range(len(a)):
        table[i, :] = np.hstack([a[i], dtable[i], b[i]])

    while(True):
        min_column = np.argmin(table[-1])
        min_line = np.argmin(table[:, -1][:-1] / table[:, min_column][:-1])

        if table[-1][min_column] >= 0:
            break

        value = table[min_line, min_column]
        if value != 1:
            table[min_line, :] /= value

        for i in range(len(table)):
            if i != min_line:
                table[i, :] += -1 * table[i, min_column] * table[min_line, :]

        basis[min_line] = min_column

    result = np.zeros(len(c))
    for i in range(len(table) - 1):
        if basis[i] >= 0:
            result[int(basis[i])] = table[i, -1]

    return result
