#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элемеiнтов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''
    #if input_list == [] or type(n) is not int:
     #   return None
    s = set(input_list)

    for i in s:
        if n-i in s:
            idx = 0
            idy = 0
            for index, val in enumerate(input_list):
                if val == i:
                    idx = index
                if val == n-i:
                    idy = index
                if idx and idy != 0:
                    return idx, idy
    return None
    raise NotImplementedError

