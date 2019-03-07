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
    for element in source_dict.values():
        extend(element)
    for i in range(len(source_dict)):
        tuple = source_dict.popitem()
        if type(tuple[1]) is list or type(tuple[1]) is set:
            for element in tuple[1]:
                if element in new_dict.keys():
                    pop = new_dict.pop(element)
                    new_dict[element] = []
                    new_dict[element].append(tuple[0])
                    new_dict[element].append(pop)
                    extend(new_dict[element])
                else:
                    new_dict[element] = tuple[0]
        else:
            if tuple[1] in new_dict.keys():
                    pop = new_dict.pop(tuple[1])
                    new_dict[tuple[1]] = []
                    new_dict[tuple[1]].append(tuple[0])
                    new_dict[tuple[1]].append(pop)
                    extend(new_dict[tuple[1]])
            else:
                new_dict[tuple[1]] = tuple[0]
    return new_dict
