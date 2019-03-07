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

    a = 0

    while a < len(input_list):
        b = a + 1
        while b < len(input_list):
            if input_list[a] + input_list[b] == n:
                break
                return tuple(a, b)
            else:
                b += 1
        if input_list[a] + input_list[b] == n:
            break
        else:
            a += 1

    raise NotImplementedError
