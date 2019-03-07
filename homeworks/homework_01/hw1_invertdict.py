#!/usr/bin/env python
# coding: utf-8


def expand(a, b):
    if (type(a) == tuple) or (type(a) == set) or (type(a) == list):
        for i in a:
            expand(i, b)
    else:
        b.append(a)


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    if not isinstance(source_dict, dict):
        return None
    else:
        new_dict = {}
        for k, a in source_dict.items():
            b = []
            expand(a, b)
            for i in range(len(b)):
                if b[i] in new_dict.keys():
                    if isinstance(new_dict[b[i]], list):
                        new_dict[b[i]].append(k)
                    else:
                        new_dict[b[i]] = [new_dict[b[i]]]
                        new_dict[b[i]].append(k)

                else:
                    new_dict[b[i]] = k
        return new_dict
    raise NotImplementedError
