#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    newdict = {}
    for k, v in source_dict.items():
        newdict.setdefault(v, []).append(k)
    return newdict
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''


print(invert_dict(dict([("key_1", "value_1"), ("key_2", "value_2")])))
