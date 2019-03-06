#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if (type(x) == (int or float)) and (type(y) == (int or float)):
        if (operator == 'plus'):
            return (x + y)
        elif operator == "minus":
            return x - y
        elif operator == "mult":
            return x * y
        elif operator == 'divide':
            if y != 0:
                return (x / y)
            else:
                return (None)
        else:
            return (None)
    else:
        return (None)
