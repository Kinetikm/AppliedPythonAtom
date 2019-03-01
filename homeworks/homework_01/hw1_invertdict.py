#!/usr/bin/env python
# coding: utf-8
import sys


def simpl(lst):
    try:
        for _ in lst:
            break
    except TypeError:
        return [lst]
    ans = []
    for i in lst:
        ans += simpl(i)
    return ans


sys.setrecursionlimit(500000)


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    ans = {}
    for key in source_dict:
        for i in simpl(source_dict[key]):
            ans[i] = []
    for key in source_dict:
        for i in simpl(source_dict[key]):
            ans[i].append(key)
    for key in ans:
        try:
            if len(ans[key]) == 1:
                ans[key] = ans[key][0]
        except KeyError:
            continue
    return ans
