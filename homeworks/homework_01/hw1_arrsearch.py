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

    sorted_list = sorted(input_list)

    left = 0
    right = len(sorted_list) - 1

    while left != right:
        sum = sorted_list[left] + sorted_list[right]
        if sum < n:
            left += 1
        elif sum > n:
            right -= 1
        else:
            return left, right

    return "None"

    raise NotImplementedError


