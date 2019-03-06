#!/usr/bin/env python
# coding: utf-8


def list_in_list(value, result_dict, key):
    if isinstance(value, (list, set, tuple)):
        for element in value:
            list_in_list(element, result_dict, key)
    else:
        if result_dict.get(value) is None:
            result_dict[value] = key
        elif isinstance(result_dict.get(value), (list, set, tuple)):
            result_dict.get(value).append(key)
        else:
            result_dict[value] = [result_dict.get(value), key]


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''

    result_dict = {}
    try:
        for key in source_dict.keys():
            list_in_list(source_dict.get(key), result_dict, key)
        return result_dict
    except AttributeError:
        return result_dict
