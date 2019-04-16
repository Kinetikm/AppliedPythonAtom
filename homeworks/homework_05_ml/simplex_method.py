#!/usr/bin/env python
# coding: utf-8

import numpy as np


def find(a, b, n):
    h = np.repeat(1000, n)
    for i in range(n):
        if a[i] > 0:
            h[i] = b[i] / a[i]
    return np.argmin(h)


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

    a = a.astype(np.float)
    b = b.astype(np.float)
    c = (-1) * c.astype(np.float)
    n, m = a.shape
    result = np.zeros(m)
    help_vector = np.repeat(-1, n)
    while c[np.argmin(c)] < 0:
        min_j = np.argmin(c)
        min_i = find(a[:, min_j], b, n)
        buf = a[min_i][min_j]
        for j in range(m):
            if j != min_j:
                c[j] -= c[min_j] * a[min_i][j] / buf
        for i in range(n):
            if i != min_i:
                b[i] -= a[i][min_j] * b[min_i] / buf
                a[i] -= a[min_i] * a[i][min_j] / buf
        a[:, min_j] = (-1) * a[:, min_j] / buf
        a[min_i] = a[min_i] / buf
        a[min_i][min_j] = 1 / buf
        b[min_i] = b[min_i] / buf
        c[min_j] = (-1) * c[min_j] / buf
        help_vector[min_i] = min_j
    for i in range(n):
        if help_vector[i] > -1:
            result[int(help_vector[i])] = b[i]
    return result
