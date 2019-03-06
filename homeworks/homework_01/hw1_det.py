#!/usr/bin/env python
# coding: utf-8


def determinant(matrix, multiplier):
    width = len(matrix)
    if width == 1:
        return multiplier * matrix[0][0]
    else:
        sign = -1
        result = 0
        for i in range(width):
            matrix_residue = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                matrix_residue.append(buff)
            sign *= -1
            result += multiplier * determinant(matrix_residue, sign * matrix[0][i])
        return result


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''

    for i in range(len(list_of_lists)):
        if len(list_of_lists[i]) != len(list_of_lists):
            return None
    if list_of_lists is [[]]:
        return None
    return determinant(list_of_lists, 1)
