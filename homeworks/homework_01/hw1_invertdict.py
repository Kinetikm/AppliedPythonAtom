#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict, new_dict=None):
    if source_dict == "":
        return {}
    if new_dict is None:
        new_dict = {}
    for key, value in source_dict.items():
        if isinstance(value, (int, str, bool)) or value == Ellipsis:
            if not (new_dict.get(value) is None):
                if type(new_dict.get(value)) == list:
                    upd = new_dict.get(value)
                    upd.append(key)
                else:
                    upd = [new_dict.get(value), key]
                new_dict.update([(value, upd)])
            else:
                new_dict.update([(value, key)])
        else:
            for each_element in value:
                new_dict = invert_dict({key: each_element}, new_dict)
    return new_dict
