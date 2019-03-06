#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    dictionary = {}
    for k, v in source_dict.items():
        dictionary[v] = dictionary.get(v, [])
        dictionary[v].append(k)
    return dictionary


# print(invert_dict({'a': 1, 'b': 2, 'c': 3, 'd': 1}))
