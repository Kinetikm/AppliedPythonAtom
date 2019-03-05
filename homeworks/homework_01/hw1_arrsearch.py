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
    res = list()
    for i in range(len(input_list)):
        tmp = input_list.copy()
        del tmp[i]
        if ((n - input_list[i]) in tmp):
            res.append(i)
            res.append(tmp.index(n - input_list[i]) + 1)
            return tuple(res)
    return None
    raise NotImplementedError
