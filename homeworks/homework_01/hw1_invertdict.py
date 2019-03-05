#!/usr/bin/env python
# coding: utf-8

def rep(list3):
    newlist = []
    for i in list3:
        if (type(i) != (list) and type(i) != (tuple) and type(i) != type(set)):
            newlist.append(i)
        else:
            newlist = newlist + rep(i)
    return newlist


def invert_dict(source_dict):
    a = {}
    b = 0
    for key, value in source_dict.items():
        # print(value)
        if (type(value) != list and type(value) != tuple and type(value) != set):
            value = [value]
        value = rep(value)
        # print(value)
        for i in value:
            # print(i,a.keys())
            if i not in a.keys():
                a[i] = key
                # print(a[i])
            else:
                # print(a[i])
                a[i] = [a[i]] + [key]
                # print(a[i],"??")

    return (a)
