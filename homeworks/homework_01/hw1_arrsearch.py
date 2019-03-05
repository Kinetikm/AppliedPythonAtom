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
    i = 0
    dictionary = dict()
    for elem in input_list:
        if elem in dictionary:
            if type(dictionary[elem]) is not list:
                dictionary[elem] = [dictionary[elem]]
            dictionary[elem].append(i)
        else:
            dictionary[elem] = i
        i += 1
    for key in dictionary:
        if (n - key) in dictionary:
            a = dictionary[key] if type(dictionary[key]) is not list else dictionary[key][0]
            b = dictionary[n - key] if type(dictionary[n - key]) is not list else dictionary[n - key][0]
            if a != b:
                return a, b
            else:
                if type(dictionary[key]) is list and len(dictionary[key]) > 1:
                    return a, dictionary[key][1]
    return None
    