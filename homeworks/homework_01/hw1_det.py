#!/usr/bin/env python
# coding: utf-8


def koef(m):
    if len(m) == 0:
        return 0
    elif len(m) == 1:
        return m.pop(0).pop(0)
    else:
        return m.pop(0).pop(0)


def calculate_determinant(m):
    '''
    width = len(m)
    sign = -1
    sum = 0
    for i in range(width):
        m = []
        for j in range(1, width):
            buff = []
            for k in range(width):
                if k != i:
                    buff.append(m[j][k])
            m.append(buff)
        sign *= -1
        sum += koef(m) * calculate_determinant(m)
    return sum
    '''
    raise NotImplementedError
