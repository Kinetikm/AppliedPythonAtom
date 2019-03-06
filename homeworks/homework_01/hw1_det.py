#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(a):
    import copy
    if a == [[]]:
        return None
    if len(a) == 1 and len(a[0]) == 1:
        b = a[0][0]
        return b
    for i in range(len(a)):
        if len(a[i]) != len(a):
            return None
    b = 0
    for i in range(len(a)):
        a1 = copy.deepcopy(a[1:])
        for ind in a1:
            del ind[i]
        b = b + a[0][i]*calculate_determinant(a1)*(-1)**i
    return b
