#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    """
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    (find_indices([2, 2], 4) == tuple([0, 1]))
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    """
    # перенос значений списка в словарь значение - индексы
    input_dict = dict()  # {}
    for i in range(len(input_list)):
        if not input_dict.get(input_list[i]):
            input_dict[input_list[i]] = []
        input_dict[input_list[i]].append(i)

    # если разница n и текущего элемента ссылается
    # на существующий элемент, то получается искомое
    for k in input_list:
        i = input_dict.get(k)  # список индексов
        j = input_dict.get(n - k)  # list

        if j:
            if i != j:
                # разные списки индексов
                return tuple([i[0], j[0]])
            elif len(i) > 1:
                # список индексов с более чем одним указателем
                return tuple([i[0], j[1]])

    return None


def find_indices_unique_list(input_list, n):
    """
    Не учитывает ситуацию с несколькими одинаковыми значениями
    (которые в рамках словаря затрут друг друга)
    (find_indices_unique_list([2, 2], 4) == None)
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    """
    input_dict = {input_list[i]: i for i in range(len(input_list))}

    # если разница n и текущего элемента ссылается
    # на существующий элемент, то получается искомое
    for k in input_list:
        i = input_dict.get(k)
        j = input_dict.get(n - k)
        if j and i != j:
            return tuple([i, j])

    return None


def find_indices_close_to_square_complexity(input_list, n):
    """
    Сложность квадратичная O(n^2)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    """
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            if input_list[i] + input_list[j] == n:
                return tuple([i, j])
    return None
