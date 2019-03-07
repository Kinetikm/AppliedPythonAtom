#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    print(list_of_lists)
    size = len(list_of_lists)
    if size > 1:
        res = 1
        for i in range(size):
            if len(list_of_lists[i])!=size:
                return None
            j = max(range(i, size), key=lambda k: abs(list_of_lists[k][i]))
            if i != j:
                list_of_lists[i], list_of_lists[j] = list_of_lists[j], list_of_lists[i]
                res *= -1
            if list_of_lists[i][i] == 0:
                return 0
            res *= list_of_lists[i][i]
            for j in range(i + 1, size):
                b = list_of_lists[j][i] / list_of_lists[i][i]
                list_of_lists[j] = [list_of_lists[j][k] - b * list_of_lists[i][k] for k in range(size)]
        return res
    else:
        try:
            if (size == len(list_of_lists[0])):
                return list_of_lists[0][0]
        except TypeError:
            return None
        except IndexError:
            return None
    return None