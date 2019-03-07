#!/usr/bin/env python
# coding: utf-8


def expand(y, l):
    if not (isinstance(y, (tuple, set, list))):
        l.append(y)
    else:
        for i in y:
            expand(i, l)


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    Dic = source_dict
    if not isinstance(Dic, dict):
        return None
    else:
        res = {}
        for x, y in Dic.items():
            l = []
            expand(y, l)
            for i in range(len(l)):
                if l[i] in res.keys():
                    if isinstance(res[l[i]], list):
                        res[l[i]].append(x)
                    else:
                        res[l[i]] = [res[l[i]]]
                        res[l[i]].append(x)
                else:
                    res[l[i]] = x
        return res
    raise NotImplementedError
