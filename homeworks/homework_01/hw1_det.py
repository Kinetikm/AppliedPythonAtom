#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(a = []):
    if len(a) == 0:
        return None
    for i in range(0, len(a)):
        if not isinstance(a[i], list) or len(a[i]) != len(a):
            return None
    if len(a) == 1:
        return a[0][0]
    det = 0
    for i in range(0, len(a)):
        minor = []
        for j in range(0, len(a) - 1):
            flag = 0
            minor.append([0] * (len(a) - 1))
            for k in range(0, len(a) - 1):
                if i == k:
                    flag = 1
                minor[j][k] = a[j+1][k+flag]
        if i%2 == 0:
            det += a[0][i] * calculate_determinant(minor)
        else:
            det -= a[0][i] * calculate_determinant(minor)
    return det
    raise NotImplementedError
