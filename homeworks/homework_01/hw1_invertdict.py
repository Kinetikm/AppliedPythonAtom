#!/usr/bin/env python
# coding: utf-8


def open(source_dict):
    """
    Функция,которая разворачивает вложенные
    друг в друга словари в один
    :param source_dict: list/set/tuple
    :return: new_list: list
    """
    new_list = []
    if isinstance(source_dict, list) or isinstance(source_dict, set) or isinstance(source_dict, tuple):
        for i in source_dict:
            new_list += open(i)
    else:
        new_list.append(source_dict)
    return new_list


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    if not isinstance(source_dict, dict):
        return None
    new_dict = {}
    for key, val in source_dict.items():
        for i in open(val):
            if i in new_dict:
                if isinstance(new_dict[i], list):
                    new_dict[i].append(key)
                else:
                    tmp = new_dict.get(i)
                    new_dict[i] = [tmp, key]
            else:
                new_dict[i] = key
    # raise NotImplementedError
