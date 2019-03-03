#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if type(x) != int and type(x) != float or type(y) != int and type(y) != float:
        return None
    if operator == "plus":
        return x+y
    if operator == "minus":
        return x-y
    if operator == "divide":
        if y != 0:
            return x/y
        else:
            return None
    if operator == "mult":
        return x*y
    else:
        return None
    raise NotImplementedError
