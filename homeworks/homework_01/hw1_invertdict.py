#!/usr/bin/env python
# coding: utf-8


def extend(lst):
    if type(lst) != list:
        return lst
    for i in range(len(lst)):
        if type(lst[i]) == list:
            extend(lst[i])
            lst.extend(lst[i])
            lst.pop(i)
    return lst


def invert_dict(source_dict):
    if type(source_dict) != dict:
        return None
    new_dict = {}
    for index in source_dict.values():
        extend(index)
    for i in range(len(source_dict)):
        key, value = source_dict.popitem()
        if isinstance(value, list) or isinstance(value, set):
            for element in value:
                if element in new_dict.keys():
                    pop = new_dict.pop(element)
                    new_dict[element] = []
                    new_dict[element].append(key)
                    new_dict[element].append(pop)
                    extend(new_dict[element])
                else:
                    new_dict[element] = key
        else:
            if value in new_dict.keys():
                    pop = new_dict.pop(value)
                    new_dict[value] = []
                    new_dict[value].append(key)
                    new_dict[value].append(pop)
                    extend(new_dict[value])
            else:
                new_dict[value] = key
    return new_dict
