#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(l_o_l):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    if len(l_o_l) == 0:
        return 0
    else:
        if (len(l_o_l) == len(l_o_l[0])):
            if len(l_o_l) == 1:
                return l_o_l[0][0]
            elif len(l_o_l) == 2:
                return l_o_l[0][0] * l_o_l[1][1] - l_o_l[0][1] * l_o_l[1][0]
            else:  # len > 2
                for i in range(len(l_o_l)):
                    l_o_l = lin_transformation(l_o_l, l_o_l[i], i + 1, i)
                    if (l_o_l is None):
                        return 0

                res = 1
                for i in range(len(l_o_l)):
                    res *= l_o_l[i][i]
                return res
        else:
            return None


# row_ind - индекс след.после row строки (С НЕГО начинать счет)
# row_col - индекс столбца, где первый ненудевой элемент
def lin_transformation(matrix, row, row_ind, col_ind):
    for i in range(row_ind, len(matrix)):
        koef = 0
        try:
            koef = matrix[i][col_ind] / row[col_ind]
        except ZeroDivisionError:
            while (matrix[i][col_ind] == 0) and (col_ind < len(matrix[i])):
                col_ind += 1
            if col_ind >= len(matrix[i]):
                return None
            else:
                koef = matrix[i][col_ind] / row[col_ind]

        matrix[i] = [aa - koef * bb for aa, bb in zip(matrix[i], row)]
    return matrix
