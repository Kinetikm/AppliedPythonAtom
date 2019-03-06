#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    if source_dict == '':
        return True
    invdict = {}
    for k, v in source_dict.items():
        invdict.setdefault(v, []).append(k)
    return invdict
