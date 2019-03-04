#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    if type(source_dict) != dict:
        return None

    new_d = {}

    def obhod(elem, struct, d):
        if type(struct) in [set, list, dict]:
            for c in struct:
                obhod(elem, c, new_d)
        elif struct not in new_d.keys():
            new_d[struct] = elem
        elif struct in new_d.keys() and type(new_d[struct]) != list:
            tmp = new_d[struct]
            new_d[struct] = []
            new_d[struct].append(tmp)
            new_d[struct].append(elem)
        else:
            new_d[struct].append(elem)

    for k, value in source_dict.items():
        obhod(k, value, source_dict)

    return new_d
