#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    di = {}
    if len(input_list) == 0:
        return None
    else:
        for i in range(len(input_list)):
            di[int(input_list[i])] = i

        for j in range(len(input_list) - 1):
            a = int(input_list[j])
            if (n - a) in di.keys() and di[n - a] != j:
                return j, di[n - a]
        return None

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

# raise NotImplementedError
