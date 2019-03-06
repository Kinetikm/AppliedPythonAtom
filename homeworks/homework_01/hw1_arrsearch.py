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
    remain_dict = {}
    for i in range(0, len(input_list)):
        remain_dict[str(n - input_list[i])] = i
    print (remain_dict)
    for k in range(0, len(input_list)):
        rem = input_list[k]
        if (str(rem) in remain_dict) and (k != remain_dict[str(rem)]):
            return (k, remain_dict[str(rem)])
    return None
