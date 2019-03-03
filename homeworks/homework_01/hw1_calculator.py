#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if not (type(x) == float and type(y) == float):
        return None
    if operator == "plus":
        return x+y
    if operator == "minus":
        return x-y
    if operator == "mult":
        return x*y
    if operator == "divide":
        if y == 0:
            return None
        return x/y
    else:
        return None
    raise NotImplementedError
