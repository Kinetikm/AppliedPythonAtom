#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    dictionary = {}
    for i in source_dict:
        value = source_dict.get(i)
        dictionary.setdefault(value, []).append(i)
    return dictionary


# print(invert_dict({'a': 1, 'b': 2, 'c': 3, 'd': 1}))
