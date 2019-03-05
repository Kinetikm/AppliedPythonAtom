#!/usr/bin/env python
# coding: utf-8


import copy
def RemoveS(matr, i, j):
    del matr[i]
    for count in range(len(matr)):
        del matr[count][j]

def calculate_determinant(list_of_lists):
    k=0
    if len(list_of_lists) > 2:
        for count in range(len(list_of_lists)):
            matr2_0=copy.deepcopy(list_of_lists)
            RemoveS(matr2_0, count, 0)
            k=k+((-1)**(count+2)) * list_of_lists[count][0] * \
              Determinant(matr2_0)
            return k
    else:
        return list_of_lists[0][0] * list_of_lists[1][1]-\
               list_of_lists[0][1] * list_of_lists[1][0]
