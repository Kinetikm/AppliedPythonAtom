#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    def internal(value, arr):
        if isinstance(value, (list, tuple, set)):
            for v in value:
                arr = (internal(v, arr))
        else:
            arr.append(value)
        return arr
    new_dict = {}
    if source_dict == '':
        return new_dict
    for key, val in source_dict.items():
        z = []
        for i in internal(val, z):
            if i in new_dict:
                if isinstance(new_dict[i], list):
                    new_dict[i].append(key)
                else:
                    new_dict[i] = [new_dict[i]]
                    new_dict[i].append(key)
            else:
                new_dict[i] = key
    return new_dict