#!/usr/bin/env python
# coding: utf-8


def det(matr, mult):
    N = len(matr)
    if N == 1:
        return mult * matr[0][0]
    else:
        s = -1
        res = 0
        for i in range(N):
            matr_ostatok = []
            for j in range(1, N):
                buff = []
                for k in range(N):
                    if k != i:
                        buff.append(matr[j][k])
                matr_ostatok.append(buff)
            s *= -1
            res += mult * det(matr_ostatok, s * matr[0][i])
        return res


def calculate_determinant(list_of_lists):
    for i in range(len(list_of_lists)):
        if len(list_of_lists) != len(list_of_lists[0]):
            return None
    if list_of_lists is None:
        return None
    return det(list_of_lists, 1)
    raise NotImplementedError
