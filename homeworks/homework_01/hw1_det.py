#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    """
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    """
    # получение размерности
    dim = len(list_of_lists)

    det = 0
    sign = 1  # знак
    i = 0
    for j in range(dim):
        # проверка что матрица квадратная
        if len(list_of_lists[i]) != dim:
            return None

        # формирование минора
        minor = []
        for k in range(dim - 1):  # i (1 - dim)
            minor.append([])
            for m in range(dim):  # j (0 - dim исключая текущий столбец)
                if m != j:
                    minor[k].append(list_of_lists[k + 1][m])

        # вычисление
        det += sign * list_of_lists[i][j] * (calculate_determinant(minor) or 1)
        sign = -sign

    return det
