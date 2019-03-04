#!/usr/bin/env python
# coding: utf-8


def help_func(key, value, new_dict):
    if type(value) == list or type(value) == tuple:
        j = 0
        while j < len(value):
            help_func(key, value[j], new_dict)
            j += 1
    else:
        h = 0
        for j in new_dict.keys():
            if j == value:
                help_list = new_dict[j]
                help_list.append(key)
                new_dict.update({value: help_list})
                h = 1
                break
        if not h:
            help_list = []
            help_list.append(key)
            new_dict.update({value: help_list})


def invert_dict(source_dict):
    new_dict = {}
    if len(source_dict) == 0:
        return source_dict
    for i in source_dict.keys():
        help_func(i, source_dict[i], new_dict)
    for i in new_dict.keys():
        if len(new_dict[i]) == 1:
            new_dict.update({i: new_dict[i][0]})
    return new_dict
    raise NotImplementedError
