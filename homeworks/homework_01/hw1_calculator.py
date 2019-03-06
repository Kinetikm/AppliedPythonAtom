#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if type(x) != int and type(x) != float:
        return None
    if type(y) != int and type(y) != float:
        return None
    if operator == "plus":
        return x+y
    elif operator == "minus":
        return x-y
    elif operator == "mult":
        return x*y
    elif operator == "divide":
        if y == 0:
            return None
        else:
            return x/y
    else:
        return None
