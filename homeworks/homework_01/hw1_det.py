#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(mat):
    from copy import deepcopy as dcopy
    if mat == [[]]:
        return None
    for i in mat:
        if len(i) != len(mat):
            return None
    if len(mat) * len(mat[0]) == 1:
        det = mat[0][0]
        return det
    det = 0
    for i in range(len(mat)):
        minor = dcopy(mat[1:])
        for j in minor:
            # print(minor)
            j.remove(j[i])
        det = det + (-1) ** i * (mat[0][i] * calculate_determinant(minor))
    return det
