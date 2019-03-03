#!/usr/bin/env python
# coding: utf-8


def calculate_minor(numCol, matrix):
    minor = []
    for index in range(1, len(matrix)):
        row = []
        if numCol == 0:
            row = matrix[index][1:]
        elif numCol == len(matrix) - 1:
            row = matrix[index][:(len(matrix) - 1)]
        else:
            row = matrix[index][:numCol] + matrix[index][numCol+1:]
        minor.append(row)
    if len(minor) == 1:
        return minor[0][0]
    if len(minor) == 2:
        return minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
    result = 0
    for index in range(0, len(minor)):
        result += (-1)**index * minor[0][index] * calculate_minor(index, minor)
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
    for row in list_of_lists:
        if len(row) != len(list_of_lists):
            return None
    if len(list_of_lists) == 1:
        return list_of_lists[0][0]
    if len(list_of_lists) == 2:
        return list_of_lists[0][0] * list_of_lists[1][1] - \
               list_of_lists[0][1] * list_of_lists[1][0]
    result = 0
    for index in range(0, len(list_of_lists)):
        result += (-1)**index * list_of_lists[0][index] * \
                  calculate_minor(index, list_of_lists)
    return result
