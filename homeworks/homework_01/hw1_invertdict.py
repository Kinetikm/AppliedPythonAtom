#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    def to_hashable_values(value):
        '''
        Функция возвращает лист из переданных значений
        :param value: any
        :return: values_list: list
        '''
        if isinstance(value, (list, set)):
            res = []
            for v in value:
                res.extend(to_hashable_values(v))
            return res
        return [value]

    if not isinstance(source_dict, dict):
        return {}
    res = {}
    for key, value in source_dict.items():
            for v in to_hashable_values(value):
                if v in res:
                    if isinstance(res[v], list):
                        res[v].append(key)
                    else:
                        res[v] = [res[v], key]
                else:
                    res[v] = key
    return res
