#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if (type(x) == float or type(x) == int)\
            and (type(y) == float or type(y) == int):
        if operator == "plus":
            return x + y
        if operator == "minus":
            return x - y
        if operator == "divide":
            if y != 0:
                return x / y
            else:
                return None
        if operator == "mult":
            return x * y
        if operator == "pow":
            return x ** y
    else:
        return None
