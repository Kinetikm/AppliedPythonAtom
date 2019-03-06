#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    dic = dict()
    j = 0
    for i in input_list:
        if i not in dic:
            dic[i] = j
        j += 1
    for i in dic:
        if n - i in dic:
            if dic[i] != dic[n - i]:
                return dic[i], dic[n - i]

    #    '''
    #    Метод возвращает индексы двух различных
    #    элементов listа, таких, что сумма этих элементов равна
    #    n. В случае, если таких элементов в массиве нет,
    #    то возвращается None
    #    Ограничение по времени O(n)
    #    :param input_list: список произвольной длины целых чисел
    #    :param n: целевая сумма
    #    :return: tuple из двух индексов или None
    #    '''
#    raise NotImplementedError
