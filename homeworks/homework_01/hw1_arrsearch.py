#!/usr/bin/env python
# coding: utf-8
from bisect import bisect_left


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
    input_dict = {}
    for index, el in enumerate(input_list):
        res = input_dict.get(n - el)
        if res is not None:
            return (index, res)
        input_dict[el] = index
    return None
