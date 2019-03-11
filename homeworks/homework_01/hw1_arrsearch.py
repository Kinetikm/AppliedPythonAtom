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
    if len(input_list) == 0:
        return None
    j = 0
    a = {}
    print("input_list = ", input_list)
    print(n)
    for x in input_list:
        if n-x in a:
            return (a[n-x], j)
        else:
            a[x] = j
        j += 1
    return None
