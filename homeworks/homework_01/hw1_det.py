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
    if n == 2:
        a = list_of_lists[0][0] * list_of_lists[1][1]
        b = list_of_lists[0][1] * list_of_lists[1][0]
        return a - b
    det = 0
    for i in range(n):
        myList = copy.deepcopy(list_of_lists)
        for j in range(1, n):
            myList[j].pop(i)
        myList.pop(0)
        det += (-1) ** (i + 2) * calculate_determinant(myList)
    return det
    raise NotImplementedError

print (calculate_determinant([[1, 2, 3], [1, 2, 4], [5, 4, 6]]))
