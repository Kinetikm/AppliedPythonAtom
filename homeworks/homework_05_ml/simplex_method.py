#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    res = [-1] * (c.shape[0])
    return solve_simplex(get_simplex_tableau(a, b, c), res)


def get_simplex_tableau(a, b, c):

    d = np.vstack((np.array(a), -np.array(c)))
    e = np.append(np.array(b), [0])
    stack = np.hstack((d, np.eye(np.size(d, 0))))
    print(np.concatenate((stack, e[:, None]), axis=1))
    return np.concatenate((stack, e[:, None]), axis=1)


def solve_simplex(table, res):
    ad = table.copy()

    j = np.where((ad[-1, :] == ad[-1].min()))
    j = int(j[0])

    b = ad[:-1, -1:]

    divided = [const / col_num for const, col_num in zip(b, ad[:-1, j])]
    i = divided.index(min(divided))

    if i in res:
        res[res.index(i)] = -1
    res[j] = i

    ad[i] = np.divide(ad[i], ad[i][j])
    to_sub = ad[i]
    coeff = ad[:, j].copy()
    coeff[i] = 0
    for i in range(ad.shape[0]):
        ad[i] = ad[i] - coeff[i] * to_sub
    if ad[-1].min() < 0:
        return solve_simplex(ad, res)

    return [ad[:, -1][val] if val != -1 else 0 for val in res]
