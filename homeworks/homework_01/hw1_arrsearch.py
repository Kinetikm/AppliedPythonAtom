#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''

    input_list.sort()

    i = 0
    i2 = 0
    j2 = len(input_list) - 1
    j = len(input_list) - 1

    while i <= j:
        if input_list[i] + input_list[j] < n:
            if i != j2:
                i += 1
            else:
                return None
        if input_list[i] + input_list[j] > n:
            if j != i2:
                j -= 1
            else:
                return None
        if (input_list[i] + input_list[j]) == n:
            return (i, j)

    return None
