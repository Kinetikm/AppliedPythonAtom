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
    i = 0
    j = 0
    for k in input_list:
        if n - k in input_list and i != input_list.index(n - k):
            a = i
            b = input_list.index(n - k)
            j = 1
            break
        i += 1
    if j:
        return tuple([a, b])
    else:
        return None
    raise NotImplementedError
