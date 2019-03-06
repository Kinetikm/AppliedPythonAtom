#!/usr/bin/env python
# coding: utf-8


def det(matrix):
    if len(matrix) == 2:
        dt = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return dt
    halfminor = matrix[1:]
    vect = matrix[0]
    dt = 0
    for i in range(len(vect)):
        minor = []
        for j in range(len(halfminor)):
            line = halfminor[j][:i] + halfminor[j][i+1:]
            minor.append(line)
        dt += (-1) ** i * vect[i] * det(minor)
    return dt


def calculate_determinant(list_of_lists):
    if len(list_of_lists) == 0:
        return None
    if len(list_of_lists) == 1:
        if len(list_of_lists[0]) == 1:
            return list_of_lists[0][0]
        else:
            return None
    for i in list_of_lists:
        if len(i) != len(list_of_lists):
            return None
    return det(list_of_lists)
