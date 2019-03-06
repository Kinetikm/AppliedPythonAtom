﻿#!/usr/bin/env python
# coding: utf-8


def check(mas):
    tmp = len(mas)
    for x in mas:
        if len(x) != tmp:
            return None
    return tmp


def deter(tens):
    if len(tens) == 2:
        return tens[0][0] * tens[1][1] - tens[1][0] * tens[0][1]
    tmp = -1
    for i in range(len(tens)):
        if tens[0][i] != 0:
            tmp = i
            break
    if tmp == -1:
        return 0
    det = tens[0][tmp]
    for i in range(1, len(tens)):
        if i == tmp:
            continue
        x = tens[0][i]/tens[0][tmp]
        for j in range(len(tens)):
            tens[j][i] -= x*tens[j][tmp]
    exp = -1 if tmp % 2 != 0 else 1
    b = tens[1:]
    b = [[b[g][k] for k in range(len(b[g]))
        if k != tmp] for g in range(len(b))]
    return exp*det*deter(b)


def calculate_determinant(list_of_lists):
    tmp = check(list_of_lists)
    if tmp is None:
        return None
    return deter(list_of_lists)
