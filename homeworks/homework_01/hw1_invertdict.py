#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    res = dict()
    for key,value in source_dict.items():
        add_to_dict(value,key,res)
    return res

def is_simple(obj):
    tp = type(obj)
    return tp==int or tp==str or tp==float

def add_to_dict(value, key, target_dict):
    if is_simple(value):
        if value in target_dict:
            if type(target_dict[value])!=list:
                target_dict[value]=[target_dict[value]]
            target_dict[value].append(key)
        else:
            target_dict[value]=key
    else:
        for item in value:
            add_to_dict(item, key, target_dict)