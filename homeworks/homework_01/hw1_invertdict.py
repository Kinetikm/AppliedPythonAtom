#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    """
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    """
    back = {}

    def pars(a):
        out = []
        for i in a:
            if type(i) is list or type(i) is set or type(i) is tuple:
                out += list(pars(i))
            else:
                out.append(i)
        return out

    for key in source_dict:
        a = source_dict[key]
        if type(a) is list or type(a) is set or type(a) is tuple:
            s = list(a)
            back[key] = pars(s)
        else:
            back[key] = a
    return back


# print(invert_dict({1 : ["sa",[2, [4] ]], 2:("sa"),3:[22]}))
