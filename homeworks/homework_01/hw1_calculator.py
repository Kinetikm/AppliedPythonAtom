#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    try:
        x, y = float(x), float(y)
    except (ValueError, TypeError, AssertionError):
        return None
    if operator == "plus":
        return x + y
    if operator == "minus":
        return x - y
    if operator == "mult":
        return x * y
    if operator == "divide":
        if y != 0:
            return x / y
        else:
            return None
    return None
    raise NotImplementedError
