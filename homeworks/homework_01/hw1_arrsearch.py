#!/usr/bin/env python
# coding: utf-8

def find_indices(input_list, n):
    c = input_list
    j = 0
    for i in c:
        if ((n - i) in c) and (n - i != i):
            c = ((input_list.index(i), input_list.index(n - i)))
            if c == ():
                return None
            return c

    else:
        return None
    