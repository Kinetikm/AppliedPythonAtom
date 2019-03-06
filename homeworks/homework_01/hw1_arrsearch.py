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
    hash_1 = {}
    for i, val in enumerate(input_list):
        hash_1[val] = i
    for i, val in enumerate(input_list):
        if (n - val) in hash_1 and hash_1[n - val] != i:
            return tuple([i, hash_1.get(n - val)])
    return None
    raise NotImplementedError
