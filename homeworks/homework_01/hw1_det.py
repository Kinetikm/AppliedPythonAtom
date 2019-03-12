#!/usr/bin/env python
# coding: utf-8
import math


def calculate_determinant(dim, list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''

    data = list_of_lists
    print(data)

    if dim == 0:
        det = 0
    if dim == 1:
        det = data[0]
    if dim == 2:
        det = data[0] * data[3] - data[2] * data[1]
    if dim == 3:
        det = data[0] * data[4] * data[8] + data[1] * data[5] * data[6] + \
              data[2] * data[3] * data[7] - data[6] * data[4] * data[2] - \
              data[7] * data[5] * data[0] - data[8] * data[3] * data[1]
    if dim > 3:
        det = 0
        i = 0
        for j in range(dim):
            det += data[i * dim + j] * alg_dopolnenie(dim, data, i, j)

    return det


def alg_dopolnenie(dim, data, i, j):
    return math.pow(-1, i + j) * dop_minor(dim, data, i, j)


def dop_minor(dim, data, i, j):
    new_matrix = []
    for k in range(dim * dim):
        if (math.floor(k / dim) != i and k % dim != j):
            new_matrix.append(data[k])
    return calculate_determinant(dim - 1, new_matrix)


listoflist111 = [[3 for i in range(5)] for k in range(5)]
listoflist112 = [[1, 2, 3, 4], [5, 25, 7, 8], [9, 10, 11, 12], [13, 14, 15, 17]]
listoflist113 = [1, 2, 3, 4, 5, 25, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17]

data = []
for i in range(len(listoflist112)):
    for j in range(len(listoflist112)):
        data = data + [listoflist112[i][j]]
dim = len(listoflist112)

print(calculate_determinant(dim, data))
