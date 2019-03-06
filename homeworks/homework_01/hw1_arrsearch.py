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

    difference_dict = {}
    for i in range(len(input_list)):
        if input_list[i] in difference_dict:
            return difference_dict.get(input_list[i]), i
        else:
            difference_dict[n-input_list[i]] = i
    return None
