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
    n, m = len(a), len(a[0])
    SimplexTable = np.zeros((n+1, m+n+2))
    Optimized_values = np.zeros(m)
    IdentityMatrix = np.eye(n + 1)

    SimplexTable[:n, :m] = a
    SimplexTable[:n+1, m:m+n+1] = IdentityMatrix
    SimplexTable[:n, -1] = b
    MaxB = b.max()
    SimplexTable[-1, :m] = -c
    Optimized_values_lines = np.full(n, -1)

    while(SimplexTable[-1].min() < 0):
        ResColumn = np.argmin(SimplexTable[-1])

        b[:] = SimplexTable[:n, -1]
        for i in range(n):
            if SimplexTable[i, ResColumn] == 0:
                b[i] = 1 + MaxB
            else:
                b[i] /= SimplexTable[i, ResColumn]
        ResLine = np.argmin(b)

        inter = SimplexTable[ResLine, ResColumn]
        if inter != 1:
            SimplexTable[ResLine, :] /= inter
        for i in range(n+1):
            if i != ResLine:
                SimplexTable[i, :] += -1 * SimplexTable[i, ResColumn] * SimplexTable[ResLine, :]
        Optimized_values_lines[ResLine] = ResColumn

    for i in range(n):
        if Optimized_values_lines[i] >= 0:
            Optimized_values[Optimized_values_lines[i]] = SimplexTable[i, -1]

    return Optimized_values
