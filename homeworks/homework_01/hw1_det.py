#!/usr/bin/env python
# coding: utf-8
import copy


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    n = len(list_of_lists)
    for myList in list_of_lists:
        if len(myList) != n:
            return None
    if n == 1:
        return list_of_lists[0][0]
    if n == 2:
        a = list_of_lists[0][0] * list_of_lists[1][1]
        b = list_of_lists[0][1] * list_of_lists[1][0]
        return a - b
    for i in range(n):
    	for j in range(i + 1, n):
    		x = (-1) * list_of_lists[j][i] / list_of_lists[i][i]
    		for k in range(n):
    			list_of_lists[j][k] += (list_of_lists[i][k] * x)
    det = 1
    for i in range(n):
    	det *= list_of_lists[i][i]
    return det
    raise NotImplementedError
print (calculate_determinant([[282.776, 264.011, 291.324], [16.077, -222.778, -175.664], [143.43, 154.597, -40.907]]))