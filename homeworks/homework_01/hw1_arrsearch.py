#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    # Метод возвращает индексы двух различных
    # элементов listа, таких, что сумма этих элементов равна
    # n. В случае, если таких элементов в массиве нет,
    # то возвращается None
    # Ограничение по времени O(n)
    # :param input_list: список произвольной длины целых чисел
    # :param n: целевая сумма
    # :return: tuple из двух индексов или None
    s = set()
    for i in range(0, len(input_list)):
        temp = n - input_list[i]
        if temp >= 0 and temp in s:
            #print("Pair with the given sum is", input_list[i], "and", temp)
            first_index = input_list.index(input_list[i])
            second_index = input_list.index(temp)
            #print("Indexes of elements of the given sum is", first_index, "and", second_index)
            return second_index, first_index
        s.add(input_list[i])

#
# A = [2, 4, 0, -6, 10, -8]
# sum = 2
# print(find_indices(A, sum))
