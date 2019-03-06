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
    dict_list = {}
    for i in range (len(input_list)):
        if input_list[i] not in dict_list:
            dict_list[input_list[i]] = i
        if n - input_list[i] in dict_list:
            return (dict_list[n - input_list[i]], i)
    return None
