#!/usr/bin/env python
# coding: utf-8


def form(key, value, new_dict):
    if isinstance(value, (list, set, tuple)):
        for val in value:
            form(key, val, new_dict)
    else:
        cur = new_dict.pop(value, None)
        if cur:
            if isinstance(cur, list):
                new_dict[value] = cur + [key]
            else:
                new_dict[value] = [cur, key]
        else:
            new_dict[value] = key
    return new_dict


def invert_dict(source_dict):
    new_dict = {}
    for key in dict(source_dict).keys():
        value = dict(source_dict).get(key)
        new_dict = form(key, value, new_dict)
    return new_dict
