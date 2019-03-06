#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):

    list_dict = {}
    for i in range(len(input_list)):
        try:
            list_dict[input_list[i]] = i
        except KeyError:
            continue

    for i in range(len(input_list)):
        found = list_dict.get(n - input_list[i])
        if found is not None:
            if found != i:
                return i, found
            else:
                continue
        else:
            continue

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
