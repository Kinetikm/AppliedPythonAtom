#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if type(x) == float and type(y) == float:
        if operator == "plus":
            return x+y
        elif operator == "minus":
            return x-y
        elif operator == "mult":
            return x*y
        elif operator == "divide" and y != 0:
            return x/y
    return None
