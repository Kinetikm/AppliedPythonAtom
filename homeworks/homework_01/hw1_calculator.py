#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    a = type(x)
    b = type(y)
    if a == int or a == float or a == complex:
        if b == int or b == float or b == complex:
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
    else:
        return None
