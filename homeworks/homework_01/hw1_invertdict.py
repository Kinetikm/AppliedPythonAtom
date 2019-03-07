#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    new_dict = {}
    for key in source_dict.keys():
        new_key = source_dict[key]
        new_value = key
        if type(new_key) == str or type(new_key) == float or type(new_key) == int:
            new_key = [new_key]
        else:
            new_key = list(new_key)
        for new_new_key in new_key:
            if new_new_key in result_d:
                new_dict[new_new_key].append(new_value)
            else:
                new_dict[new_new_key] = [new_value]
    return new_dict
