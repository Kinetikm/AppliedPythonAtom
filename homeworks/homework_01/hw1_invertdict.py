#!/usr/bin/env python
# coding: utf-8


def open_value(value):
    myList = []
    if type(value) is set or type(value) is tuple or type(value) is list:
        for item in value:
            myList += open_value(item)
    else:
        return [value]
    return myList


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    myDict = {}

    for key in source_dict:
        openedValue = open_value(source_dict[key])
        for item in openedValue:
            try:
                myDict[item].append(key)
            except KeyError:
                myDict[item] = key
            except AttributeError:
                myDict[item] = [myDict[item]]
                myDict[item].append(key)
    return myDict
