#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
        for i in input_list:
                k = n - i
                if k in input_list and input_list.index(i) != input_list.index(k):
                        a = (input_list.index(i), input_list.index(k))
                return a
        return None
