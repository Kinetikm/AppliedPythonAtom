#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    s = set()
    for i in range(0, len(input_list)):
        temp = n - input_list[i]
        if temp >= 0 and temp in s:
            first_index = input_list.index(input_list[i])
            second_index = input_list.index(temp)
            return second_index, first_index
        s.add(input_list[i])

print(find_indices([],0))