#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    d = dict()#создаем пустой словарь
    
    s = input_list
    i = 0
    t = 0
    for elem in s:
        t = n - elem
        if t in d:
            return (i, d[t])
        elif t not in d:
            d[elem] = i
        i+=1
    return None
    raise NotImplementedError
