#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    if not isinstance(source_dict, dict):
        return None
    intended_dict = {}
    for k, v in source_dict.items():
        for i in v:
            intended_dict.setdefault(i, []).append(k)
    return intended_dict
