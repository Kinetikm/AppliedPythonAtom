#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    ans = {}
    for key in source_dict:
        try:
            for i in source_dict[key]:
                ans[i] = []
        except TypeError:
            ans[source_dict[key]] = []
    for key in source_dict:
        try:
            for i in source_dict[key]:
                ans[i].append(key)
        except TypeError:
            ans[source_dict[key]].append(key)
    for key in ans:
        try:
            if len(ans[key]) == 1:
                ans[key] = ans[key][0]
        except KeyError:
            continue
    return ans
