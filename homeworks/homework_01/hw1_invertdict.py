#!/usr/bin/env python
# coding: utf-8

def invert_dict(source_dict):
    def internal(value):
        internal_arr = []
        if isinstance(value, (list, tuple, set)):
            for v in value:
                internal_arr.append(internal(v))
        else:
            internal_arr.append(value)
        return internal_arr

    new_dict = {}
    for key, val in source_dict.items():
        for i in internal(val):
            if i in new_dict:
                if isinstance(new_dict[i], list):
                    new_dict[i].append(key)
                else:
                    new_dict[i] = [new_dict[i]]
                    new_dict[i].append(key)
            else:
                new_dict[i] = key
    return new_dict
