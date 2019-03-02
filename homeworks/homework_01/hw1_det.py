#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(a):
    """
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param a: список списков - исходная матрица
    :return: значение определителя или None
    """
    for i in range(len(a)):
        if len(a[i]) != len(a):
            return None
    res = 1
    n = len(a)
    for i in range(n):
        # выбираем опорный элемент
        j = max(range(i, n), key=lambda k: abs(a[k][i]))
        if i != j:
            a[i], a[j] = a[j], a[i]
            res *= -1
        # убеждаемся, что матрица не вырожденная
        if a[i][i] == 0:
            return 0
        res *= a[i][i]
        # "обнуляем" элементы в текущем столбце
        for j in range(i + 1, n):
            b = a[j][i] / a[i][i]
            a[j] = [a[j][k] - b * a[i][k] for k in range(n)]
    return res
