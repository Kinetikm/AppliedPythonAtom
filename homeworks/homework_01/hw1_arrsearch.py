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
    print(input_list)
    j = 0
    i = None
    for x in input_list:
        a = n-x
        i = input_list.index(a) if a in input_list else None
        if i is not None and i != j:
            break
        j += 1
    if i is not None and i != j:
        print(i, j)
        return (i, j)
    else:
        return None
