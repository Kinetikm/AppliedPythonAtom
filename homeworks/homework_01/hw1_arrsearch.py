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
    tmp1 = []
    tmp1 = input_list
    len1 = len(tmp1)
    for i in range(len1):
        tmp2 = n - tmp1[i]
        asd = tmp1.index(tmp2)
        if (asd != 0):
            return i, asd
    return None

