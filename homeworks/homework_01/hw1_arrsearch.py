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
    d = {}
    i = 0
    for k in input_list:
        if n - k in d.keys():
            A = (i, d[n - k])
            break
        else:
            d[k] = i
            A = None
        i += 1
    return A
    raise NotImplementedError
