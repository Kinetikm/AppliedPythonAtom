#!/usr/bin/env python
# coding: utf-8


def reveal(value):
    '''
    Returns list of values with revealing
    of lists and making list from not list value
    :param value: some value
    :return: list of values in
    '''
    containers = [list, set]
    resultList = []
    if type(value) not in containers:
        resultList = [value]
    else:
        for elem in value:
            if type(value) not in containers:
                resultList.append(elem)
            else:
                for deepElem in reveal(elem):
                    resultList.append(deepElem)
    return resultList


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    if type(source_dict) != dict:
        return source_dict
    inversedDict = dict()
    for pair in source_dict.items():
        for value in reveal(pair[1]):
            if value not in inversedDict:
                inversedDict[value] = pair[0]
            else:
                if type(inversedDict[value]) != list:
                    inversedDict[value] = [inversedDict[value]]
                inversedDict[value].append(pair[0])
    return inversedDict
