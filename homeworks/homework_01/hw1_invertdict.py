#!/usr/bin/env python
# coding: utf-8

'''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
'''


def list_opener(inlist):
    easylist = []
    for i in inlist:
        if type(i) == list:
            easylist.extend(list_opener(i))
        else:
            easylist.append(i)
    return easylist


def tuple_opener(intup):
    easytup = []
    for i in intup:
        if type(i) == tuple:
            easytup.extend(tuple_opener(i))
        else:
            easytup.append(i)
    return tuple(easytup)


def invert_dict(source_dict):
    print(source_dict)
    if type(source_dict) == dict:
        new_dict = {}
        for i in source_dict.keys():
            keys = []
            if type(source_dict[i]) == list:
                keys = list_opener(source_dict[i])
                temp_dict = dict.fromkeys(keys, i)
            elif type(source_dict[i]) == set:
                temp_dict = dict.fromkeys(source_dict[i], i)
            elif type(source_dict[i]) == tuple:
                keys = tuple_opener(source_dict[i])
                temp_dict = dict.fromkeys(keys, i)
            else:
                temp_dict = {source_dict[i]: i}
            for i in temp_dict.keys():
                if new_dict.get(i) is not None:
                    templist = []
                    templist.append(new_dict.get(i))
                    templist.append(temp_dict.get(i))
                    temp_dict[i] = templist
            new_dict.update(temp_dict)
        for i in new_dict.keys():
            if type(new_dict[i]) == list:
                new_dict[i] = list_opener(new_dict[i])
        return new_dict
    else:
        return source_dict
