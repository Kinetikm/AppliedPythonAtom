#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    def calculate_determinant(list_of_lists):
    if len(list_of_lists) == 0:
        return None
    for l in list_of_lists:
        if len(l) != len(list_of_lists):
            return None
    det = 0
    if len(list_of_lists) == 1:
        return list_of_lists[0][0]
    if len(list_of_lists) == 2:
        return list_of_lists[0][0]*list_of_lists[1][1]\
            -list_of_lists[1][0]*list_of_lists[0][1]
    if len(list_of_lists) > 2:
        i = 0
        while i < len(list_of_lists):
            sup_matr = list_of_lists[::]
            sup_matr.pop(0)
            j = 0
            while j < len(sup_matr):
                sup_matr[j].pop(i)
                j += 1
            det += list_of_lists[0][i]*(1**i)*\
                calculate_determinant(sup_matr)
            i += 1
        return det
