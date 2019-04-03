#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    c *= -1
    a = a.astype(np.float)
    b = b.astype(np.float)
    c = c.astype(np.float)
    n, m = a.shape
    help_array = np.zeros(n)
    while True:
        c_min = np.min(c)
        if c_min >= 0:
            break
        j_of_min = np.argmin(c)
        copy_of_b = np.copy(b)
        copy_of_b = copy_of_b/a[:, j_of_min]
        i_of_min = np.argmin(copy_of_b)
        b[i_of_min] /= a[i_of_min][j_of_min]
        a[i_of_min] = a[i_of_min]/a[i_of_min][j_of_min]
        i = 0
        while i < n:
            if i != i_of_min:
                b[i] -= b[i_of_min]*a[i][j_of_min]
                a[i] -= a[i_of_min]*a[i][j_of_min]
            i += 1
        c -= a[i_of_min]*c[j_of_min]
        help_array[i_of_min] = j_of_min+1
    result = np.zeros(m)
    i = 0
    while i < n:
        if help_array[i] != 0:
            result[int(help_array[i])-1] = b[i]
        i += 1
    return result
