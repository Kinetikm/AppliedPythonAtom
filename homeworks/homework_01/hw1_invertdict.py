#!/usr/bin/env python
# coding: utf-8


def invert_dict(dic):
    if not isinstance(dic, dict):
        return dic
    reverse_dict = {}

    def relist(list1):
        newlist = []
        for letter in list1:
            if not isinstance(letter, (list, tuple, set)):
                newlist.append(letter)
            else:
                newlist = newlist + relist(letter)
        return newlist

    for key, value in dic.items():
        if not isinstance(value, (list, tuple, set)):
            value = [value]
        value = relist(value)
        for val in value:
            reverse_dict[val] = reverse_dict.get(val, [])
            reverse_dict[val].append(key)
    for key, value in reverse_dict.items():
        if len(value) == 1:
            reverse_dict[key] = value[0]
    return reverse_dict
