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
    size = len(input_list)
    dictionary = {i: [] for i in input_list}
    for i in range(size):
        dictionary[input_list[i]].append(i)
    for i in range(size):
        if input_list[i] * 2 != n:
            if n - input_list[i] in dictionary:
                return i, dictionary[n - input_list[i]][0]
        else:
            if len(dictionary[input_list[i]] >= 2):
                return i, dictionary[input_list[i]][1]
    return None
