#!/usr/bin/env python
# coding: utf-8


def det(mat, mul):
    size = len(mat)
    if size != 1:
        sgn = -1
        s = 0
        for i in range(size):
            m = []
            for j in range(1, size):
                buff = []
                for k in range(size):
                    if k != i:
                        buff.append(mat[j][k])
                m.append(buff)
            sgn *= -1
            s += mul * det(m, sgn * mat[0][i])
        return s
    else:
        return mul * mat[0][0]


def calculate_determinant(list_of_lists):
    if list_of_lists == [[]] or len(list_of_lists) != len(list_of_lists[0]):
        return None
    else:
        return det(list_of_lists, 1)
    raise NotImplementedError
