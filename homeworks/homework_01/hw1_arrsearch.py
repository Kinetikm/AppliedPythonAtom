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
    mp = {}
    for i in range(size):
        try:
            mp[input_list[i]].append(i)
        except KeyError:
            mp[input_list[i]] = [i]
    for i in range(size):
        if n - input_list[i] != input_list[i]:
            try:
                return i + 1, mp[n - input_list[i]][0] + 1
            except KeyError:
                continue
        else:
            if len(mp[input_list[i]]) > 1:
                return mp[input_list[i]][0] + 1, mp[input_list[i]][1] + 1
    return None
