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
    for i in range(len(input_list)):
        if (n-input_list[i]) in input_list:
            if input_list[i] != n-input_list[i]:
                output_turp = (i, input_list.index(n-input_list[i]))
                return output_turp
    return None
    raise NotImplementedError
