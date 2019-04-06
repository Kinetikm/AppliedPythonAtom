#!/usr/bin/env python
# coding: utf-8

import numpy as np


def find_index_i(a, b, n):
    h = np.tile(np.inf, n)
    for i in range(n):
        if a[i] > 0:
            h[i] = b[i]/a[i]
    return np.argmin(h)


def simplex_method(a, b, c):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    c = (-1)*np.array(c, dtype=float)
    n, m = a.shape
    Arguments = np.zeros(m)
    buffer = np.tile(-1, n)
    while c[np.argmin(c)] < 0:
        index_j = np.argmin(c)
        index_i = find_index_i(a[:, index_j], b,  n)
        Buf = a[index_i][index_j]
        for j in range(m):
            if j != index_j:
                c[j] -= c[index_j] * a[index_i][j]/Buf
        for i in range(n):
            if i != index_i:
                b[i] -= a[i][index_j] * b[index_i]/Buf
                a[i] -= a[index_i]*a[i][index_j]/Buf
        b[index_i] = b[index_i]/Buf
        a[:, index_j] = a[:, index_j]/(Buf*(-1))
        a[index_i] /= Buf
        a[index_i][index_j] = 1/Buf
        c[index_j] /= ((-1)*Buf)
        buffer[index_i] = index_j
    for i in range(n):
        if buffer[i] != -1:
            Arguments[int(buffer[i])] = b[i]
    return Arguments
