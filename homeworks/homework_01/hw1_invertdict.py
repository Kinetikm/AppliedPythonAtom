#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    myDict = {}
    for key in source_dict:
    	myDict[source_dict[key]] = key
    return myDict
    raise NotImplementedError
