#!/usr/bin/env python
# coding: utf-8


def invert_dict(dict1):
    intended_dict ={}
    try:
        for k, v in dict1.items():
            for i in v:
                intended_dict.setdefault(i, []).append(k)
    except (AttributeError,TypeError):
        return dict1
    else:
        return intended_dict
