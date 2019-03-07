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
    l=input_list
    res=tuple()
    for i in range(len(l)):
        if n-l[i] in l:
            if (n-l[i] != l[i]):
                res=(i,l.index(n-l[i]))
                return res
    return None
print(find_indices((1,2,3,4,5,6,7,8,9,10),11))
