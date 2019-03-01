#!/usr/bin/env python
# coding: utf-8


def invert(source):
    """
    Функция разворачивающая вложенные
    друг в друга словари в один
    :param source: list, tuple or set
    :return: new: list
    """
    new = []

    if not source:
        return new

    if isinstance(source, set):
        new = [i for i in source]
    else:
        new = source[::]

    i = 0
    while i < len(new):
        if isinstance(new[i], (list, tuple)):
            item = new.pop(i)
            new += item
        else:
            i += 1

    return new


def invert_dict(source_dict):
    """
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    """
    new_dict = {}

    if not source_dict:
        return new_dict

    for key, value in source_dict.items():
        if isinstance(value, (list, tuple, set)):
            for val in invert(value):
                if new_dict.get(val):
                    if isinstance(new_dict.get(val), list):
                        new_dict[val].append(key)
                    else:
                        new_dict[val] = [new_dict[val], key]
                else:
                    new_dict[val] = key
        else:
            if new_dict.get(value):
                if isinstance(new_dict.get(value), list):
                    new_dict[value].append(key)
                else:
                    new_dict[value] = [new_dict[value], key]
            else:
                new_dict[value] = key

    return new_dict
