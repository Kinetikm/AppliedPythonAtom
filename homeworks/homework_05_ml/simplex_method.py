#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https:// https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
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
    a = a.astype('float64')
    b = b.astype('float64')
    c = c.astype('float64')
    c = -1 * c
    while not (c >= 0).all():
        column_with_min_in_c = c.argmin()
        row_with_min_in_a = (b / a[:, column_with_min_in_c]).argmin()
        b[row_with_min_in_a] = b[row_with_min_in_a] / a[
            row_with_min_in_a, column_with_min_in_c]
        a[row_with_min_in_a] = a[row_with_min_in_a, :] / a[
            row_with_min_in_a, column_with_min_in_c]
        for i in range(a.shape[0]):
            if i != row_with_min_in_a:
                b[i] = -b[row_with_min_in_a] * a[i, column_with_min_in_c] + b[
                    i]
                a[i] = -a[i, column_with_min_in_c] * a[row_with_min_in_a] + a[
                    i]
        c = -c[column_with_min_in_c] * a[
            row_with_min_in_a] + c
    a[:, np.where(c > 0)[0]] = 0
    x = b.T @ a
    return x
