#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    i = 0
    j = False
    for k in input_list:
        if n - k in input_list and i != input_list.index(n - k):
            a = i
            b = input_list.index(n - k)
            j = True
            break
        i += 1
    if j:
        return [a, b]
    else:
        return False
    raise NotImplementedError


print(find_indices([1, 2, 3, 4, 5, 6], 11))
