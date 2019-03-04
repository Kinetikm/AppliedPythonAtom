#!/usr/bin/env python
# coding: utf-8
import copy


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''

    def add_key(dictionary, val, key):
        if val in dictionary:
            if type(dictionary[val]) is list:
                dictionary[val].append(key)
            else:
                dictionary[val] = [dictionary[val]] + [key]
        else:
            dictionary[val] = key
        return dictionary

    def rekurs(res, element, k):
        if type(element) is list or type(element) is tuple or \
                type(element) is set:
            for elem in element:
                res = rekurs(res, copy.deepcopy(elem), k)
        else:
            res = add_key(res, copy.deepcopy(element), source_key)
        return res

    result = dict()
    for source_key in (source_dict):
        source_val = source_dict[source_key]
        result = rekurs(result, copy.deepcopy(source_val), source_key)

    return result
