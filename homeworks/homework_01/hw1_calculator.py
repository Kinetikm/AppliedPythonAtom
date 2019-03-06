#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if not(isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return None
    if operator == "plus":
        x = x + y
        return x
    elif operator == "minus":
        x = x - y
        return x
    elif operator == "mult":
        x = x * y
        return x
    elif operator == "divide":
        if y == 0:
            return None
        x = x / y
    else:
        return None
    return x
    raise NotImplementedError
