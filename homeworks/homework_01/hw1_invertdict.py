#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''

    inv_map = {}

    if not source_dict:
        return source_dict

    for k, v in source_dict.items():
        if isinstance(v, (list, tuple, set)):
            flat_list = []
            f1(v, flat_list)
            for v2 in flat_list:
                if v2 in inv_map:
                    if not isinstance(inv_map[v2], list):
                        tmp = inv_map[v2]
                        inv_map[v2] = [tmp]
                    inv_map[v2].append(k)
                else:
                    inv_map[v2] = k
        else:
            if v in inv_map:
                if not isinstance(inv_map[v], list):
                    tmp = inv_map[v]
                    inv_map[v] = [tmp]
                inv_map[v].append(k)
            else:
                inv_map[v] = k

    return inv_map


def f1(strct, flat_list):
    for sublist in strct:
        if isinstance(sublist, (list, tuple, set)):
            f1(sublist, flat_list)
        else:
            flat_list.append(sublist)
