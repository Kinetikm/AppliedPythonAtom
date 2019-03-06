#!/usr/bin/env python
# coding: utf-8


def rep(list3):
    newlist = []
    for i in list3:
        if type(i) != list and type(i) != tuple and type(i) != set:
            newlist.append(i)
        else:
            newlist = newlist + rep(i)
    return newlist


def invert_dict(source_dict):
    if not isinstance(source_dict, dict):
        return source_dict
    a = {}
    b = 0
    for key, value in source_dict.items():
        if type(value) != list and type(value) != tuple and type(value) != set:
            value = [value]
        value = rep(value)
        for i in value:
            if i not in a.keys():
                a[i] = key
            else:
                a[i] = [a[i]] + [key]

    return (a)
