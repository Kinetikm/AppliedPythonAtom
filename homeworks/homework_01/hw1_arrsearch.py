#!/usr/bin/env python
# coding: utf-8


# def find_indices(input_list, n):
#     s = set()
#     for i in range(0, len(input_list)):
#         temp = n - input_list[i]
#         if temp >= 0 and temp in s:
#             first_index = input_list.index(temp)
#             second_index = input_list.index(input_list[i])
#             return first_index, second_index
#         s.add(input_list[i])
#     return None
def find_indices(input_list, n):
    """
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    """
    # create dictionary{num:ind} without indexes
    dictionary = {number: [] for number in input_list}
    print(dictionary)
    print('----------')
    # add indexes for every number
    for i in range(len(input_list)):
        dictionary[input_list[i]].append(i)
        print(dictionary)
    # actually finding any matching pair
    for i in range(len(input_list)):
        # no need to find same element
        if input_list[i] * 2 != n:
            # find matching element
            if n - input_list[i] in dictionary:
                # current index and closest index of match
                return i, dictionary[n - input_list[i]][0]
        # may find same element
        else:
            # means 2 same elements there are in list
            if len(dictionary[input_list[i]]) >= 2:
                # return current elements index and closest
                return i, dictionary[input_list[i]][1]
    return None
