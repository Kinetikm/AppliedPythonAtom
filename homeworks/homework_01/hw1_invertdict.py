#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    print(source_dict)
    if source_dict == '':
        return ''
    d = source_dict
    newdict = {}
    for x, val in d.items():
        print("val =", val)
#        for x in d.keys():
        if isinstance(val, list):
            print("list")
            for val_list in flatten(val):
                newdict.setdefault(val_list, []).append(x)
        elif isinstance(val, tuple):
            print("tuple")
            for val_tuple in val:
                newdict.setdefault(val_tuple, []).append(x)
        elif isinstance(val, set):
            print("set")
            for val_set in val:
                newdict.setdefault(val_set, []).append(x)
        else:
            print("else")
            newdict.setdefault(val, []).append(x)
    for x, val in newdict.items():
        if isinstance(val, list):
            if len(val) == 1:
                newdict[x] = val[0]
    return newdict
    #  raise NotImplementedError


def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
