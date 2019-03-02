#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    def minor(matrix, j):
        return matrix[j][0], [row[1:] for row in matrix[:j] + matrix[j + 1:]]

    def determinant(matrix):
        if len(matrix) == 1:
            return matrix[0][0]
        res = 0
        for j in range(len(matrix)):
            a, mm = minor(matrix, j)
            res += (-1) ** (j) * a * determinant(mm)
        return res
    m = len(list_of_lists)
    for l in list_of_lists:
        if len(l) != m:
            return None
    return determinant(list_of_lists)
