#!/usr/bin/env python
# coding: utf-8


def merge(in_list):
    for ele in in_list:
        if (type(ele) == list):
            merge(ele)
        else:
            res.append(ele)


res = []


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    if (source_dict == ""):
        return True

    new_dict = {}
    for k, v in source_dict.items():
        if type(v) == list:
            res.clear()
            merge(v)

            for vs in res:
                if new_dict.get(vs):
                    new_dict[vs].append(k)
                else:
                    new_dict[vs] = [k]
        elif type(v) == set:
            for vs in v:
                if new_dict.get(vs):
                    new_dict[vs].append(k)
                else:
                    new_dict[vs] = [k]

        else:
            if new_dict.get(v):
                new_dict[v].append(k)
            else:
                new_dict[v] = [k]

    for k, v in new_dict.items():
        if (len(v) == 1):
            new_dict[k] = v[0]
    return new_dict