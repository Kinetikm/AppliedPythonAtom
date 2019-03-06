#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    invdict = {}
    for k, v in source_dict.items():
        invdict.setdefault(v, []).append(k)
    return invdict


# print(invert_dict({'a': 3, 'c': 2, 'b': 2, 'e': 3, 'd': 1, 'f': 2}))
