#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    input_list.sort()
    left = 0
    right = len(input_list) - 1
    while right > left:
        if (input_list[left]+input_list[right]) == n:
            return left, right
        if (input_list[left]+input_list[right]) < n:
            left += 1
        if (input_list[left]+input_list[right]) > n:
            right -= 1
    return None
