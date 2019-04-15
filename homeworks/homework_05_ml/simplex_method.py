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
    solution = [None] * a.shape[0]
    spl_tab = np.vstack((a, c*(-1)))
    add_mtx = np.vstack((np.eye(a.shape[0]), np.zeros((1, a.shape[0]))))
    spl_tab = np.hstack((spl_tab, add_mtx))
    add_col = np.hstack((b.transpose(), np.zeros(1)))
    spl_tab = np.hstack((spl_tab, add_col.reshape((add_col.shape[0], 1))))
    while True:
        min_elem = np.amin(spl_tab[-1, :])
        if min_elem >= 0:
            break
        min_col = np.argmin(spl_tab[-1, :])
        spl_rel = np.zeros(spl_tab.shape[0] - 1)
        for i in range(0, spl_tab.shape[0] - 1):
            if np.isclose(spl_tab[i, min_col], 0):
                spl_rel[i] = np.inf
            else:
                spl_rel[i] = spl_tab[i, -1] / spl_tab[i, min_col]
        min_row = np.argmin(spl_rel)
        solution[min_row] = min_col
        for i in range(0, spl_tab.shape[0]):
            delta = spl_tab[i, min_col] / spl_tab[min_row, min_col]
            min_elem = spl_tab[min_row, min_col]
            for k in range(0, spl_tab.shape[1]):
                if i == min_row:
                    spl_tab[i, k] = spl_tab[i, k] / min_elem
                else:
                    spl_tab[i, k] = spl_tab[i, k] - spl_tab[min_row, k]*delta
    x = np.zeros(a.shape[1])
    for i in range(0, len(solution)):
        if solution[i] is not None:
            if solution[i] < a.shape[1]:
                x[solution[i]] = spl_tab[i, -1]
    return x
