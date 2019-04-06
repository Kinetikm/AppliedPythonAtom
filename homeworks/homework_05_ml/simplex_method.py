#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    a = a.astype(dtype=float)
    b = b.astype(dtype=float)
    c = -c.astype(dtype=float)

    n, m = a.shape
    matrix = np.append(a, [c], axis=0)
    matrix = np.append(matrix, np.eye(n + 1), axis=1)
    last = np.append(b, [0], axis=0).reshape(n+1, 1)
    matrix = np.append(matrix, last, axis=1)  # добавляем столбец b c 0 в конце

    while min(matrix[-1, :]) < 0:
        pivot_column = np.argmin(matrix, axis=1)[-1]  # индекс минимального в последней строке (разрешающий столбец)
        # делим все элементы последнего столбца на элементы разрешающего столбца и возвращаем индекс минимального
        pivot_row = np.argmin(matrix[:, -1][:-1] / matrix[:, pivot_column][:-1])

        matrix[pivot_row, :] /= matrix[pivot_row, pivot_column]
        for i in range(n+1):  # получаем нули для элементов кроме текущего в разрешающем столбце
            if i != pivot_row:
                matrix[i, :] -= matrix[pivot_row, :] * matrix[i, pivot_column]

    res = []
    for i in range(m):
        if len(np.nonzero(matrix[:, i])[0]) == 1:
            # возвращаем индекс первого ненулевого элемента в текущем столбце
            first_non_zero = np.nonzero(matrix[:, i])[0]
            # добавляем элемент в последнем столбце с найденным индексом
            res = np.append(res, matrix[first_non_zero, -1])
        else:
            res = np.append(res, [0])
    return np.array(res)
