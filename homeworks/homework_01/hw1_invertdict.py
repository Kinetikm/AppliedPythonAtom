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

    def go_deeper(obj):
        if not isinstance(obj, (set, tuple, list)):
            if obj in new_dict:
                if type(new_dict[obj]) != list:
                    templist = []
                    templist.append(new_dict[obj])
                    new_dict[obj] = templist
                new_dict[obj].append(k)
            else:
                new_dict[obj] = k
            return None
        else:
            for elem in obj:
                go_deeper(elem)
    for k in source_dict:
        go_deeper(source_dict[k])
    return new_dict
