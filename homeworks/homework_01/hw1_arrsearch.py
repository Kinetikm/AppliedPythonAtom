#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    input_list.sort()
    i, j = 0, len(input_list) - 1
    print(i, j)
    while i != j:
        try:
            sum = input_list[i] + input_list[j]
            print(sum)
        except IndexError:
            return None
        if sum < n:
            i += 1
        if sum > n:
            j -= 1
        if sum == n:
            if i != j:
                return i, j
            return None
    return None
