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
    for i in range(len(list_of_lists)):
        if len(list_of_lists[i]) != len(list_of_lists):
            return None
    res = 1
    n = len(list_of_lists)
    for i in range(n):
        # выбираем опорный элемент
        j = max(range(i, n), key=lambda k: abs(list_of_lists[k][i]))
        if i != j:
            list_of_lists[i], list_of_lists[j] = list_of_lists[j], list_of_lists[i]
            res *= -1
        # убеждаемся, что матрица не вырожденная
        if list_of_lists[i][i] == 0:
            return 0
        res *= list_of_lists[i][i]
        # "обнуляем" элементы в текущем столбце
        for j in range(i + 1, n):
            b = list_of_lists[j][i] / list_of_lists[i][i]
            list_of_lists[j] = [
                list_of_lists[j][k] - b * list_of_lists[i][k] for k in range(n)
            ]
    return res
